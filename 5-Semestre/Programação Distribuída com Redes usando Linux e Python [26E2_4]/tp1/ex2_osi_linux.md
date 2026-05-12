# Exercício 2 - OSI Aplicado ao Linux

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M:%S")  
**Sistema:** Kali Linux (VirtualBox)

## Tabela OSI × Comandos Linux

| Comando                                       | Camada OSI                          | Justificativa |
|-----------------------------------------------|-------------------------------------|-------------|
| `ip link`                                     | 1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:8a:35:d2 brd ff:ff:ff:ff:ff:ff
              |             |
| `arp -n`                                      | Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.2.2                 ether   52:54:00:12:35:00   C                     eth0              |             |
| `ip addr`                                     | (Rede1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:8a:35:d2 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute eth0
       valid_lft 82519sec preferred_lft 82519sec
    inet6 fd17:625c:f037:2:2713:216d:9399:9a8a/64 scope global dynamic noprefixroute 
       valid_lft 86050sec preferred_lft 14050sec
    inet6 fe80::cf4b:6e86:7b2d:d13a/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
)                 |             |
| `ping`                                        | ping: usage error: Destination address required              |             |
| `ss -tuln`                                    | Netid           State             Recv-Q            Send-Q                            Local Address:Port                        Peer Address:Port           
udp             UNCONN            0                 0                                       0.0.0.0:500                              0.0.0.0:*              
udp             UNCONN            0                 0                                       0.0.0.0:4500                             0.0.0.0:*              
udp             UNCONN            0                 0                                          [::]:500                                 [::]:*              
udp             UNCONN            0                 0                                             *:43058                                  *:*              
udp             UNCONN            0                 0                                             *:36496                                  *:*              
udp             UNCONN            0                 0                                          [::]:4500                                [::]:*              
tcp             LISTEN            0                 50                           [::ffff:127.0.0.1]:38825                                  *:*              
tcp             LISTEN            0                 50                                        [::1]:38453                               [::]:*              
tcp             LISTEN            0                 1                            [::ffff:127.0.0.1]:43421                                  *:*              
tcp             LISTEN            0                 1                            [::ffff:127.0.0.1]:41017                                  *:*           |             |
| `netstat -tuln`                               | Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp6       0      0 127.0.0.1:38825         :::*                    LISTEN     
tcp6       0      0 ::1:38453               :::*                    LISTEN     
tcp6       0      0 127.0.0.1:43421         :::*                    LISTEN     
tcp6       0      0 127.0.0.1:41017         :::*                    LISTEN     
udp        0      0 0.0.0.0:500             0.0.0.0:*                          
udp        0      0 0.0.0.0:4500            0.0.0.0:*                          
udp6       0      0 :::500                  :::*                               
udp6       0      0 :::43058                :::*                               
udp6       0      0 :::36496                :::*                               
udp6       0      0 :::4500                 :::*                               
                                                              |             |
| `who`                                         | kali     seat0        2026-05-10 18:01 (:0)
          |             |
| `openssl s_client -connect google.com:443`    | Connecting to 142.250.78.206
CONNECTED(00000003)
depth=2 C=US, O=Google Trust Services LLC, CN=GTS Root R1
verify return:1
depth=1 C=US, O=Google Trust Services, CN=WR2
verify return:1
depth=0 CN=*.google.com
verify return:1
---
Certificate chain
 0 s:CN=*.google.com
   i:C=US, O=Google Trust Services, CN=WR2
   a:PKEY: EC, (prime256v1); sigalg: sha256WithRSAEncryption
   v:NotBefore: Apr 20 08:35:05 2026 GMT; NotAfter: Jul 13 08:35:04 2026 GMT
 1 s:C=US, O=Google Trust Services, CN=WR2
   i:C=US, O=Google Trust Services LLC, CN=GTS Root R1
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT
 2 s:C=US, O=Google Trust Services LLC, CN=GTS Root R1
   i:C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA
   a:PKEY: RSA, 4096 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Jun 19 00:00:42 2020 GMT; NotAfter: Jan 28 00:00:42 2028 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIONzCCDR+gAwIBAgIRAPIuzR8E/lf+CrPMiIpFXf0wDQYJKoZIhvcNAQELBQAw
OzELMAkGA1UEBhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczEM
MAoGA1UEAxMDV1IyMB4XDTI2MDQyMDA4MzUwNVoXDTI2MDcxMzA4MzUwNFowFzEV
MBMGA1UEAwwMKi5nb29nbGUuY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE
is27tRmO/bLFj/9YzOy+hlpp+jCFXRxZxwiNiv+wHQ9dEI4ALF2RnYpL3owQBDt4
/7JrhwEzOJF/dS53p3hP56OCDCMwggwfMA4GA1UdDwEB/wQEAwIHgDATBgNVHSUE
DDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBTHbJqmLrmV5vaD
jcFVjXKmoHTQyTAfBgNVHSMEGDAWgBTeGx7teRXUPjckwyG77DQ5bUKyMDBYBggr
BgEFBQcBAQRMMEowIQYIKwYBBQUHMAGGFWh0dHA6Ly9vLnBraS5nb29nL3dyMjAl
BggrBgEFBQcwAoYZaHR0cDovL2kucGtpLmdvb2cvd3IyLmNydDCCCfgGA1UdEQSC
Ce8wggnrggwqLmdvb2dsZS5jb22CFiouYXBwZW5naW5lLmdvb2dsZS5jb22CCSou
YmRuLmRldoIVKi5vcmlnaW4tdGVzdC5iZG4uZGV2ghIqLmNsb3VkLmdvb2dsZS5j
b22CGCouY3Jvd2Rzb3VyY2UuZ29vZ2xlLmNvbYIYKi5kYXRhY29tcHV0ZS5nb29n
bGUuY29tggsqLmdvb2dsZS5jYYILKi5nb29nbGUuY2yCDiouZ29vZ2xlLmNvLmlu
gg4qLmdvb2dsZS5jby5qcIIOKi5nb29nbGUuY28udWuCDyouZ29vZ2xlLmNvbS5h
coIPKi5nb29nbGUuY29tLmF1gg8qLmdvb2dsZS5jb20uYnKCDyouZ29vZ2xlLmNv
bS5jb4IPKi5nb29nbGUuY29tLm14gg8qLmdvb2dsZS5jb20udHKCDyouZ29vZ2xl
LmNvbS52boILKi5nb29nbGUuZGWCCyouZ29vZ2xlLmVzggsqLmdvb2dsZS5mcoIL
Ki5nb29nbGUuaHWCCyouZ29vZ2xlLml0ggsqLmdvb2dsZS5ubIILKi5nb29nbGUu
cGyCCyouZ29vZ2xlLnB0gg8qLmdvb2dsZWFwaXMuY26CDCouZ3N0YXRpYy5jboIQ
Ki5nc3RhdGljLWNuLmNvbYIPZ29vZ2xlY25hcHBzLmNughEqLmdvb2dsZWNuYXBw
cy5jboIRZ29vZ2xlYXBwcy1jbi5jb22CEyouZ29vZ2xlYXBwcy1jbi5jb22CDGdr
ZWNuYXBwcy5jboIOKi5na2VjbmFwcHMuY26CEmdvb2dsZWRvd25sb2Fkcy5jboIU
Ki5nb29nbGVkb3dubG9hZHMuY26CEHJlY2FwdGNoYS5uZXQuY26CEioucmVjYXB0
Y2hhLm5ldC5jboIQcmVjYXB0Y2hhLWNuLm5ldIISKi5yZWNhcHRjaGEtY24ubmV0
ggt3aWRldmluZS5jboINKi53aWRldmluZS5jboIRYW1wcHJvamVjdC5vcmcuY26C
EyouYW1wcHJvamVjdC5vcmcuY26CEWFtcHByb2plY3QubmV0LmNughMqLmFtcHBy
b2plY3QubmV0LmNughdnb29nbGUtYW5hbHl0aWNzLWNuLmNvbYIZKi5nb29nbGUt
YW5hbHl0aWNzLWNuLmNvbYIXZ29vZ2xlYWRzZXJ2aWNlcy1jbi5jb22CGSouZ29v
Z2xlYWRzZXJ2aWNlcy1jbi5jb22CEWdvb2dsZXZhZHMtY24uY29tghMqLmdvb2ds
ZXZhZHMtY24uY29tghFnb29nbGVhcGlzLWNuLmNvbYITKi5nb29nbGVhcGlzLWNu
LmNvbYIVZ29vZ2xlb3B0aW1pemUtY24uY29tghcqLmdvb2dsZW9wdGltaXplLWNu
LmNvbYISZG91YmxlY2xpY2stY24ubmV0ghQqLmRvdWJsZWNsaWNrLWNuLm5ldIIY
Ki5mbHMuZG91YmxlY2xpY2stY24ubmV0ghYqLmcuZG91YmxlY2xpY2stY24ubmV0
gg5kb3VibGVjbGljay5jboIQKi5kb3VibGVjbGljay5jboIUKi5mbHMuZG91Ymxl
Y2xpY2suY26CEiouZy5kb3VibGVjbGljay5jboIRZGFydHNlYXJjaC1jbi5uZXSC
EyouZGFydHNlYXJjaC1jbi5uZXSCHWdvb2dsZXRyYXZlbGFkc2VydmljZXMtY24u
Y29tgh8qLmdvb2dsZXRyYXZlbGFkc2VydmljZXMtY24uY29tghhnb29nbGV0YWdz
ZXJ2aWNlcy1jbi5jb22CGiouZ29vZ2xldGFnc2VydmljZXMtY24uY29tghdnb29n
bGV0YWdtYW5hZ2VyLWNuLmNvbYIZKi5nb29nbGV0YWdtYW5hZ2VyLWNuLmNvbYIY
Z29vZ2xlc3luZGljYXRpb24tY24uY29tghoqLmdvb2dsZXN5bmRpY2F0aW9uLWNu
LmNvbYIkKi5zYWZlZnJhbWUuZ29vZ2xlc3luZGljYXRpb24tY24uY29tghZhcHAt
bWVhc3VyZW1lbnQtY24uY29tghgqLmFwcC1tZWFzdXJlbWVudC1jbi5jb22CC2d2
dDEtY24uY29tgg0qLmd2dDEtY24uY29tggtndnQyLWNuLmNvbYINKi5ndnQyLWNu
LmNvbYILMm1kbi1jbi5uZXSCDSouMm1kbi1jbi5uZXSCFGdvb2dsZWZsaWdodHMt
Y24ubmV0ghYqLmdvb2dsZWZsaWdodHMtY24ubmV0ggxhZG1vYi1jbi5jb22CDiou
YWRtb2ItY24uY29tghkqLmdlbWluaS5jbG91ZC5nb29nbGUuY29tghRnb29nbGVz
YW5kYm94LWNuLmNvbYIWKi5nb29nbGVzYW5kYm94LWNuLmNvbYIeKi5zYWZlbnVw
Lmdvb2dsZXNhbmRib3gtY24uY29tgg0qLmdzdGF0aWMuY29tghQqLm1ldHJpYy5n
c3RhdGljLmNvbYIKKi5ndnQxLmNvbYIRKi5nY3BjZG4uZ3Z0MS5jb22CCiouZ3Z0
Mi5jb22CDiouZ2NwLmd2dDIuY29tghAqLnVybC5nb29nbGUuY29tghYqLnlvdXR1
YmUtbm9jb29raWUuY29tggsqLnl0aW1nLmNvbYIKYWkuYW5kcm9pZIILYW5kcm9p
ZC5jb22CDSouYW5kcm9pZC5jb22CEyouZmxhc2guYW5kcm9pZC5jb22CBGcuY26C
BiouZy5jboIEZy5jb4IGKi5nLmNvggZnb28uZ2yCCnd3dy5nb28uZ2yCFGdvb2ds
ZS1hbmFseXRpY3MuY29tghYqLmdvb2dsZS1hbmFseXRpY3MuY29tggpnb29nbGUu
Y29tghJnb29nbGVjb21tZXJjZS5jb22CFCouZ29vZ2xlY29tbWVyY2UuY29tgghn
Z3BodC5jboIKKi5nZ3BodC5jboIKdXJjaGluLmNvbYIMKi51cmNoaW4uY29tggh5
b3V0dS5iZYILeW91dHViZS5jb22CDSoueW91dHViZS5jb22CEW11c2ljLnlvdXR1
YmUuY29tghMqLm11c2ljLnlvdXR1YmUuY29tghR5b3V0dWJlZWR1Y2F0aW9uLmNv
bYIWKi55b3V0dWJlZWR1Y2F0aW9uLmNvbYIPeW91dHViZWtpZHMuY29tghEqLnlv
dXR1YmVraWRzLmNvbYIFeXQuYmWCByoueXQuYmWCGmFuZHJvaWQuY2xpZW50cy5n
b29nbGUuY29tghMqLmFuZHJvaWQuZ29vZ2xlLmNughIqLmNocm9tZS5nb29nbGUu
Y26CFiouZGV2ZWxvcGVycy5nb29nbGUuY26CFSouYWlzdHVkaW8uZ29vZ2xlLmNv
bTATBgNVHSAEDDAKMAgGBmeBDAECATA2BgNVHR8ELzAtMCugKaAnhiVodHRwOi8v
Yy5wa2kuZ29vZy93cjIvb0JGWVlhaHpnVkkuY3JsMIIBBQYKKwYBBAHWeQIEAgSB
9gSB8wDxAHYA1219ENGn9XfCx+lf1wC/+YLJM1pl4dCzAXMXwMjFaXcAAAGdqj5k
nwAABAMARzBFAiBlfn5cVV6+Vqur2t5g7mcqFKnY0ONUo1hp1f9WSGmY3QIhAOzh
uGdM5FINtmxwIsPllrtmQFKhV8t8UKxdFZ6FeJKfAHcAyKPEf8ezrbk1awE/anoS
beM6TkOlxkb5l605dZkdz5oAAAGdqj5ktAAABAMASDBGAiEA5D+gxqeAN67822ml
EgEsa42u587nnscOW4X/n/HJukUCIQDxQHnfj3pJ9duiSTyI286ala6TtXqGXhHW
lIgTN38QQzANBgkqhkiG9w0BAQsFAAOCAQEABRL26vEDFOPtG+PnzfA8YcH7gEqf
NOo5E8gu9uM9DNxXotVP99cebi5npELVfNmMvUiALQ+4HXlXOTHHDkCm1wFX/ieN
xTP4DpBrecTyam9AbJGaXHZ1aKvCmbIaI2nAsuaNRc+4w09QSrgHu51PhBG8h6q0
PRdojaP/FtaO9EL5HVrSi4U6mFcgY7T2kWvIdmdK/ldTUgumPZmccUFgxRP0fLEW
C2Xp7r8VWPjcLuepUaP8wyBujgFtVfR/5ISF6BknwND3ygTlHSONvtKQwQzxEqMC
KW4WqVqr/dTDm7jDup4cDRTJ2URLLKbf3oFqxddeSgiQn+cd6CusrUH+fQ==
-----END CERTIFICATE-----
subject=CN=*.google.com
issuer=C=US, O=Google Trust Services, CN=WR2
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: ecdsa_secp256r1_sha256
Negotiated TLS1.3 group: X25519MLKEM768
---
SSL handshake has read 7723 bytes and written 1757 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Protocol: TLSv1.3
Server public key is 256 bit
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---

^X
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 519A31FFC909AEBD1A81275FC02CC9804A9E2EA0F0B50D8AFA25DA1CF9186D68
    Session-ID-ctx: 
    Resumption PSK: 1D36687359B174261259920E3FC06176DBF41B619E178173F4D93114983FCCA2A47524B3395AA8EB7287FCDB5FDB3C89
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 172800 (seconds)
    TLS session ticket:
    0000 - 02 09 f4 7d 3f c1 92 72-f0 73 64 86 1b 04 2d 1c   ...}?..r.sd...-.
    0010 - 08 67 8d 1c f5 c6 c0 c3-a5 fd aa 44 25 9a ec f5   .g.........D%...
    0020 - 63 77 8d 40 e5 73 31 c5-96 fa ba dd bf 02 11 26   cw.@.s1........&
    0030 - cf 48 b4 a1 78 0d f6 e1-7c 16 c4 f9 84 62 87 f3   .H..x...|....b..
    0040 - 03 a4 ea 50 91 17 82 7a-a5 78 d1 6b 87 4b 3c 57   ...P...z.x.k.K<W
    0050 - ac 91 5e 00 40 78 39 39-d9 35 ac 4c 8e 11 c6 8f   ..^.@x99.5.L....
    0060 - 16 69 f6 55 9f 54 c3 93-ee 6a 3c cb 05 c1 45 b7   .i.U.T...j<...E.
    0070 - 90 e2 fe 9c 06 bb ab 50-d3 f8 1d 43 1a 4f cc c1   .......P...C.O..
    0080 - e4 96 88 73 ba 4e c0 d8-57 48 b9 b2 02 7f 5c d9   ...s.N..WH....\.
    0090 - 9d b2 37 31 bd 26 a1 f9-df e5 b4 e3 26 0d cd b9   ..71.&......&...
    00a0 - b9 85 1f d1 23 35 8a 30-9d de f4 17 47 45 5a 01   ....#5.0....GEZ.
    00b0 - 63 cb ee 75 08 8f a9 fd-44 ef c7 7f f8 1a 08 21   c..u....D......!
    00c0 - 29 ef 22 e3 08 bc 24 7c-58 f9 e4 60 51 81 8c ef   )."...$|X..`Q...
    00d0 - dc 15 26 fe b7 5d a2 47-b3 45 9e 43 de 6a 42 89   ..&..].G.E.C.jB.
    00e0 - 38 3a d0 f5 ca 78 f0 b7-02 a1 3d 52 49 4f 44 ab   8:...x....=RIOD.
    00f0 - 33 66 6c 78 65 47                                 3flxeG

    Start Time: 1778454696
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 14336
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 8D66B3D7E356F49C3E6112570CE524B00D180377AB6CD61E79F1122EE079A3EB
    Session-ID-ctx: 
    Resumption PSK: 0FFE73A28F882424D996D1C6CED055C0A7C80A4441CA29649CBD90E8757C40C63CD8D615AF1B0EE7C2C7F7416C33339B
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 172800 (seconds)
    TLS session ticket:
    0000 - 02 09 f4 7d 3f c1 92 72-f0 73 64 86 1b 04 2d 1c   ...}?..r.sd...-.
    0010 - e0 4a 15 84 61 05 24 1d-01 99 dd 51 23 82 a2 91   .J..a.$....Q#...
    0020 - e3 cb 7f 07 8e eb e8 4d-cf 0b 1f 45 43 70 d9 37   .......M...ECp.7
    0030 - 48 81 7a 10 16 d4 31 3c-04 c1 14 3d 24 15 08 b8   H.z...1<...=$...
    0040 - ba cb 7c c8 f9 98 37 b7-13 1c 5f ac b0 a1 cd 1a   ..|...7..._.....
    0050 - 4b ca f6 70 2d e1 14 ac-52 22 f8 ae ed fd d9 95   K..p-...R"......
    0060 - 70 c2 bc 2e 78 7c 68 1a-5d 96 9e ae 5e d3 07 5f   p...x|h.]...^.._
    0070 - 6c 53 31 b8 dc ce bb a6-2a 8e 0f f1 1b 96 b0 b3   lS1.....*.......
    0080 - 90 f9 0a 8b 00 6f 29 9a-3d f2 b4 73 53 7e 39 96   .....o).=..sS~9.
    0090 - d5 94 af 91 7d 63 70 c2-0c c7 33 c9 14 1c 3b 86   ....}cp...3...;.
    00a0 - 71 e1 76 63 67 87 44 ce-82 ff fa 03 c5 7e 54 f5   q.vcg.D......~T.
    00b0 - 60 79 be bd 3b b7 34 e8-4b 66 29 6a 16 57 5e 61   `y..;.4.Kf)j.W^a
    00c0 - 52 cc 7f 16 df 5d 2a b6-c9 2e 44 0d 03 3a 48 c4   R....]*...D..:H.
    00d0 - 46 7d e7 d1 be 48 e1 26-d5 1a 13 31 14 50 84 1e   F}...H.&...1.P..
    00e0 - 58 f4 07 e4 d5 88 e6 f3-04 52 dd 52 49 4f 01 5f   X........R.RIO._
    00f0 - 54 98 46 1a 3f dc                                 T.F.?.

    Start Time: 1778454696
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 14336
---
read R BLOCK
HTTP/1.0 400 Bad Request
Content-Length: 54
Content-Type: text/html; charset=UTF-8
Date: Sun, 10 May 2026 23:12:08 GMT

<html><title>Error 400 (Bad Request)!!1</title></html>40D7CA3BB37F0000:error:0A000126:SSL routines::unexpected eof while reading:../ssl/record/rec_layer_s3.c:698:
40D7CA3BB37F0000:error:0A000197:SSL routines:SSL_shutdown:shutdown while in init:../ssl/ssl_lib.c:2804: |             |
| `wget`                                        | wget: missing URL
Usage: wget [OPTION]... [URL]...

Try `wget --help' for more options.
           |             |

