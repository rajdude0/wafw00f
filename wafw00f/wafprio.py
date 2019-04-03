#!/usr/bin/env python

# NOTE: this priority list is used so that each check can be prioritized,
# so that the quick checks are done first and ones that require more
# requests, are done later


wafdetectionsprio = [
    # cached default request ones first
    'Edgecast / Verizon Digital media',
    'Profense',
    'PowerCDN',
    'ChinaCache-CDN',
    'West263CDN',
    'AdNovum nevisProxy',
    'NetContinuum',
    'CloudFlare',
    'NSFocus',
    'DOSarrest',
    'Comodo WAF',
    'XLabs Security WAF',
    'Wallarm',
    'BlockDoS',
    'Mission Control Application Shield',
    'USP Secure Entry Server',
    'Cisco ACE XML Gateway',
    'Art of Defence HyperGuard',
    'BinarySec',
    'Teros WAF',
    # the next ones require attack strings to be sent
    'Barracuda Application Firewall',
    'Safedog',
    'Naxsi',
    'Radware AppWall',
    'FortiWeb',
    'Sucuri WAF',
    'Incapsula WAF',
    '360WangZhanBao',
    'Anquanbao',
    'F5 BIG-IP LTM',
    'F5 BIG-IP APM',
    'F5 BIG-IP ASM',
    'F5 FirePass',
    'F5 Trafficshield',
    'AWS WAF',
    'Ergon Airlock',
    'Citrix NetScaler',
    'IBM DataPower',
    'Trustwave ModSecurity',
    'IBM Web Application Security',
    'DenyALL WAF',
    'Applicure dotDefender',
    'Microsoft URLScan',
    'Aqtronix WebKnight',
    'eEye Digital Security SecureIIS',
    'Imperva SecureSphere',
    'Better WP Security',
    'Wordfence',
    'Microsoft ISA Server',
]