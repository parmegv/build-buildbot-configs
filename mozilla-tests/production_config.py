SLAVES = {
    'xp-ix': {},
    'win7-ix': {},
    'win8': {},
    'snowleopard': {},
    'mountainlion': {},
    'yosemite': {},
    'panda_android': {},
    'ubuntu32_vm': {},
    'ubuntu64_vm': {},
    'ubuntu64_vm_large': {},
    'ubuntu32_hw': {},
    'ubuntu64_hw': {},
    'win64_vm': {},
}

for i in range(1, 163):
    SLAVES['xp-ix']['t-xp32-ix-%03i' % i] = {}

for i in range(1, 163):
    SLAVES['win7-ix']['t-w732-ix-%03i' % i] = {}

for i in range(1, 171):
    SLAVES['win8']['t-w864-ix-%03i' % i] = {}

for i in range(1, 166):
    SLAVES['snowleopard']['t-snow-r4-%04i' % i] = {}

for i in range(1, 14):
    SLAVES['mountainlion']['talos-mtnlion-r5-%03i' % i] = {}

for i in range(1, 29) + range(29, 94):
    SLAVES['yosemite']['t-yosemite-r5-%04i' % i] = {}

for i in range(22, 910):
    SLAVES['panda_android']['panda-%04i' % i] = {
        'http_port': '30%03i' % i,
        'ssl_port': '31%03i' % i,
    }

for i in range(1, 100) + range(300, 360):
    SLAVES['ubuntu32_vm']['tst-linux32-ec2-%03i' % i] = {}

for i in range(1, 800) + range(1000, 1100):
    SLAVES['ubuntu32_vm']['tst-linux32-spot-%03i' % i] = {}

for i in range(1, 100) + range(301, 400):
    SLAVES['ubuntu64_vm']['tst-linux64-ec2-%03i' % i] = {}

for i in range(1, 20):
    SLAVES['ubuntu64_vm_large']['tst-emulator64-ec2-%03i' % i] = {}

for i in range(1, 200) + range(301, 500):
    SLAVES['ubuntu64_vm_large']['tst-emulator64-spot-%03i' % i] = {}

for i in range(1, 2100):
    SLAVES['ubuntu64_vm']['tst-linux64-spot-%03i' % i] = {}

for i in range(1, 56):
    SLAVES['ubuntu32_hw']['talos-linux32-ix-%03i' % i] = {}

for i in range(1, 120):
    SLAVES['ubuntu64_hw']['talos-linux64-ix-%03i' % i] = {}

for i in range(1, 3):
    SLAVES['win64_vm']['tst-w64-ec2-%03i' % i] = {}

SLAVES['ubuntu64-asan_vm'] = SLAVES['ubuntu64_vm']
# Use "-b2g" suffix to make misc.py generate unique builder names
SLAVES['ubuntu32_vm-b2gdt'] = SLAVES['ubuntu32_vm']
SLAVES['ubuntu64_vm-b2g'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2gdt'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-lg-emulator'] = SLAVES['ubuntu64_vm_large']
SLAVES['ubuntu64_vm-b2g-emulator-jb'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm-b2g-emulator-kk'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_hw-b2g'] = SLAVES['ubuntu64_hw']
SLAVES['mountainlion-b2gdt'] = SLAVES['mountainlion']
SLAVES['win8_64'] = SLAVES['win8']
SLAVES['ubuntu64_vm_mobile'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm_armv7_mobile'] = SLAVES['ubuntu64_vm']
SLAVES['ubuntu64_vm_armv7_large'] = SLAVES['ubuntu64_vm_large']

TRY_SLAVES = {}

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
                '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'disable_tinderbox_mail': True,
    'build_tools_repo_path': 'build/tools',
    'mozharness_repo': 'https://hg.mozilla.org/build/mozharness',
    'mozharness_tag': 'production',
    'stage_server': 'stage.mozilla.org',
    'stage_username': 'ffxbld',
    'stage_ssh_key': 'ffxbld_rsa',
    'datazilla_url': 'https://datazilla.mozilla.org/talos',
    'blob_upload': True,
}


# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'tinderbox_tree': 'Firefox',
        'mobile_tinderbox_tree': 'Firefox',
    },
    'mozilla-release': {
        'tinderbox_tree': 'Mozilla-Release',
        'mobile_tinderbox_tree': 'Mozilla-Release',
    },
    'mozilla-esr31': {
        'tinderbox_tree': 'Mozilla-Esr31',
        'mobile_tinderbox_tree': 'Mozilla-Esr31',
    },
    'mozilla-esr38': {
        'tinderbox_tree': 'Mozilla-Esr38',
        'mobile_tinderbox_tree': 'Mozilla-Esr38',
    },
    'mozilla-b2g32_v2_0': {
        'tinderbox_tree': 'Mozilla-B2g32-v2.0',
        'mobile_tinderbox_tree': 'Mozilla-B2g32-v2.0',
    },
    'mozilla-b2g34_v2_1': {
        'tinderbox_tree': 'Mozilla-B2g34-v2.1',
        'mobile_tinderbox_tree': 'Mozilla-B2g34-v2.1',
    },
    'mozilla-b2g34_v2_1s': {
        'tinderbox_tree': 'Mozilla-B2g34-v2.1s',
        'mobile_tinderbox_tree': 'Mozilla-B2g34-v2.1s',
    },
    'mozilla-b2g37_v2_2': {
        'tinderbox_tree': 'Mozilla-B2g37-v2.2',
        'mobile_tinderbox_tree': 'Mozilla-B2g37-v2.2',
    },
    'mozilla-beta': {
        'tinderbox_tree': 'Mozilla-Beta',
        'mobile_tinderbox_tree': 'Mozilla-Beta',
    },
    'mozilla-aurora': {
        'tinderbox_tree': 'Mozilla-Aurora',
        'mobile_tinderbox_tree': 'Mozilla-Aurora',
    },
    'addontester': {
        'tinderbox_tree': 'AddonTester',
        'mobile_tinderbox_tree': 'AddonTester',
    },
    'addonbaselinetester': {
        'tinderbox_tree': 'AddonTester',
        'mobile_tinderbox_tree': 'AddonTester',
    },
    'try': {
        'tinderbox_tree': 'Try',
        'mobile_tinderbox_tree': 'Try',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'enable_merging': False,
        'slave_key': 'try_slaves',
        'package_url': 'https://ftp-ssl.mozilla.org/pub/mozilla.org/firefox/try-builds',
        'package_dir': '%(who)s-%(got_revision)s',
        'stage_username': 'trybld',
        'stage_ssh_key': 'trybld_dsa',
    },
}

PLATFORM_VARS = {
}

PROJECTS = {
    'jetpack': {
        'scripts_repo': 'https://hg.mozilla.org/build/tools',
        'tinderbox_tree': 'Jetpack',
    },
}
B2G_PROJECTS = {}
