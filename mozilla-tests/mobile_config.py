from copy import deepcopy

import config_common
reload(config_common)
from config_common import TALOS_CMD, loadDefaultValues, loadCustomTalosSuites, loadTalosSuites

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS, GRAPH_CONFIG

REMOTE_PROCESS_NAMES = {'default': 'org.mozilla.fennec',
                        'mozilla-beta': 'org.mozilla.firefox_beta',
                        'mozilla-aurora': 'org.mozilla.fennec_aurora',
                        'mozilla-release': 'org.mozilla.firefox',
                        'release-mozilla-beta': 'org.mozilla.firefox_beta',
                        'release-mozilla-release': 'org.mozilla.firefox',
                        }

TALOS_REMOTE_FENNEC_OPTS = {'productName': 'fennec',
                            'remoteTests': True,
                            'remoteExtras': {'options': ['--sampleConfig', 'remote.config',
                                                         '--output', 'local.yml',
                                                         '--webServer', 'bm-remote.build.mozilla.org',
                                                         '--browserWait', '60',
                                                         ],
                                             'processName': REMOTE_PROCESS_NAMES,
                                             },
                            }

UNITTEST_REMOTE_EXTRAS = {'processName': REMOTE_PROCESS_NAMES}
ANDROID_UNITTEST_REMOTE_EXTRAS = deepcopy(UNITTEST_REMOTE_EXTRAS)
ANDROID_UNITTEST_REMOTE_EXTRAS['cmdOptions'] = ['--bootstrap']

BRANCHES = {
    'mozilla-central':     {},
    'mozilla-aurora':      {},
    'mozilla-release':     {},
    'mozilla-beta':        {},
    'mozilla-esr17':       {
        'datazilla_url': None,
        'platforms': {},
        'lock_platforms': True,
    },
    'mozilla-b2g18': {
        'datazilla_url': None,
        'platforms': {
            'android-noion': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g18_v1_0_0': {
        'datazilla_url': None,
        'platforms': {
            'android-noion': {},
        },
        'lock_platforms': True,
    },
    'mozilla-b2g18_v1_0_1': {
        'datazilla_url': None,
        'platforms': {
            'android-noion': {},
        },
        'lock_platforms': True,
    },
    'try': {'coallesce_jobs': False},
}

# Talos
PLATFORMS = {
    'android': {},
    'android-armv6': {},
    'android-noion': {},
}

PLATFORMS['android']['slave_platforms'] = ['tegra_android', 'panda_android']
PLATFORMS['android']['env_name'] = 'android-perf'
PLATFORMS['android']['is_mobile'] = True
PLATFORMS['android']['tegra_android'] = {'name': "Android Tegra 250"}
PLATFORMS['android']['panda_android'] = {'name': "Android 4.0 Panda"}
PLATFORMS['android']['stage_product'] = 'mobile'
PLATFORMS['android']['mozharness_config'] = {}

PLATFORMS['android-armv6']['slave_platforms'] = ['tegra_android-armv6']
PLATFORMS['android-armv6']['env_name'] = 'android-perf'
PLATFORMS['android-armv6']['is_mobile'] = True
PLATFORMS['android-armv6']['tegra_android-armv6'] = {'name': "Android Armv6 Tegra 250"}
PLATFORMS['android-armv6']['stage_product'] = 'mobile'
PLATFORMS['android-armv6']['mozharness_config'] = {}

PLATFORMS['android-noion']['slave_platforms'] = ['tegra_android-noion']
PLATFORMS['android-noion']['env_name'] = 'android-perf'
PLATFORMS['android-noion']['is_mobile'] = True
PLATFORMS['android-noion']['tegra_android-noion'] = {'name': "Android no-ionmonkey Tegra 250"}
PLATFORMS['android-noion']['stage_product'] = 'mobile'
PLATFORMS['android-noion']['mozharness_python'] = '/tools/buildbot/bin/python'


# Lets be explicit instead of magical.
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

ANDROID = PLATFORMS['android']['slave_platforms']

SUITES = {
    'remote-ts': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts', '--mozAfterPaint', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tsvg': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvg', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tsspider': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsspider', '--noChrome'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-trobopan': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'trobopan', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-trobocheck': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tcheckerboard', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-troboprovider': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tprovider', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-trobocheck2': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tcheck2', '--noChrome', '--fennecIDs', '../fennec_ids.txt'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tp4m_nochrome': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4m', '--noChrome', '--rss'],
        'options': (TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
}

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'android': {},
        'android-armv6': {},
        'android-noion': {},
    },
}


ANDROID_UNITTEST_DICT = {
    'opt_unittest_suites': [
        ('mochitest-1', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 1,
             },
        )),
        ('mochitest-2', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 2,
             },
        )),
        ('mochitest-3', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 3,
             },
        )),
        ('mochitest-4', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 4,
             },
        )),
        ('mochitest-5', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 5,
             },
        )),
        ('mochitest-6', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 6,
             },
        )),
        ('mochitest-7', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 7,
             },
        )),
        ('mochitest-8', (
            {'suite': 'mochitest-plain',
             'testManifest': 'android.json',
             'totalChunks': 8,
             'thisChunk': 8,
             },
        )),
        ('reftest-1', (
            {'suite': 'reftest',
             'totalChunks': 4,
             'thisChunk': 1,
             },
        )),
        ('reftest-2', (
            {'suite': 'reftest',
             'totalChunks': 4,
             'thisChunk': 2,
             },
        )),
        ('reftest-3', (
            {'suite': 'reftest',
             'totalChunks': 4,
             'thisChunk': 3,
             },
        )),
        ('reftest-4', (
            {'suite': 'reftest',
             'totalChunks': 4,
             'thisChunk': 4,
             },
        )),
        # disabled for constant timeouts, bug 728119
        # ('crashtest-1', (
        #     {'suite': 'crashtest',
        #      'totalChunks': 3,
        #      'thisChunk': 1,
        #      },
        # )),
        ('crashtest-2', (
            {'suite': 'crashtest',
             'totalChunks': 3,
             'thisChunk': 2,
             },
        )),
        ('crashtest-3', (
            {'suite': 'crashtest',
             'totalChunks': 3,
             'thisChunk': 3,
             },
        )),
        ('jsreftest-1', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 1,
             },
        )),
        ('jsreftest-2', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 2,
             },
        )),
        ('jsreftest-3', (
            {'suite': 'jsreftest',
             'totalChunks': 3,
             'thisChunk': 3,
             },
        )),
        ('robocop', (
            {'suite': 'mochitest-robocop',
             },
        )),
    ],
    'debug_unittest_suites': [],
}

ANDROID_NOION_UNITTEST_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}
for suite in ANDROID_UNITTEST_DICT['opt_unittest_suites']:
    if not suite[0].startswith('jsreftest'):
        continue
    ANDROID_NOION_UNITTEST_DICT['opt_unittest_suites'].append(suite)

ANDROID_ARMV6_UNITTEST_DICT = deepcopy(ANDROID_UNITTEST_DICT)

ANDROID_PLAIN_UNITTEST_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}

ANDROID_PLAIN_REFTEST_DICT = {
    'opt_unittest_suites': [
        ('plain-reftest-1', (
            {'suite': 'reftestsmall',
             'totalChunks': 4,
             'thisChunk': 1,
             'extra_args': '--ignore-window-size'
             },
        )),
        ('plain-reftest-2', (
            {'suite': 'reftestsmall',
             'totalChunks': 4,
             'thisChunk': 2,
             'extra_args': '--ignore-window-size'
             },
        )),
        ('plain-reftest-3', (
            {'suite': 'reftestsmall',
             'totalChunks': 4,
             'thisChunk': 3,
             'extra_args': '--ignore-window-size'
             },
        )),
        ('plain-reftest-4', (
            {'suite': 'reftestsmall',
             'totalChunks': 4,
             'thisChunk': 4,
             'extra_args': '--ignore-window-size'
             },
        )),
    ],
}


for suite in ANDROID_UNITTEST_DICT['opt_unittest_suites']:
    if suite[0].startswith('reftest'):
        continue
    ANDROID_PLAIN_UNITTEST_DICT['opt_unittest_suites'].append(suite)

for suite in ANDROID_PLAIN_REFTEST_DICT['opt_unittest_suites']:
    ANDROID_PLAIN_UNITTEST_DICT['opt_unittest_suites'].append(suite)
ANDROID_PANDA_UNITTEST_DICT = {
    'opt_unittest_suites': [],
    'debug_unittest_suites': [],
}
for suite in ANDROID_PLAIN_UNITTEST_DICT['opt_unittest_suites']:
    if suite[0].startswith('reftest') or suite[0].startswith('plain-reftest'):
        continue
    ANDROID_PANDA_UNITTEST_DICT['opt_unittest_suites'].append(suite)

# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
    'android': {
        'product_name': 'fennec',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'is_remote': True,
        'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.%%(foopy_type)s.742597.zip',
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'remote_extras': ANDROID_UNITTEST_REMOTE_EXTRAS,
        'tegra_android': deepcopy(ANDROID_PLAIN_UNITTEST_DICT),
        'panda_android': deepcopy(ANDROID_PANDA_UNITTEST_DICT),
    },
    'android-armv6': {
        'product_name': 'fennec',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'is_remote': True,
        'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.%%(foopy_type)s.742597.zip',
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'remote_extras': ANDROID_UNITTEST_REMOTE_EXTRAS,
        'tegra_android-armv6': deepcopy(ANDROID_ARMV6_UNITTEST_DICT),
    },
    'android-noion': {
        'product_name': 'fennec',
        'app_name': 'browser',
        'brand_name': 'Minefield',
        'is_remote': True,
        'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.%%(foopy_type)s.742597.zip',
        'enable_opt_unittests': True,
        'enable_debug_unittests': False,
        'remote_extras': ANDROID_UNITTEST_REMOTE_EXTRAS,
        'tegra_android-noion': deepcopy(ANDROID_NOION_UNITTEST_DICT),
    },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])
    if BRANCHES[branch].get('mobile_platforms'):
        BRANCHES[branch]['platforms'] = deepcopy(BRANCHES[branch]['mobile_platforms'])

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # In order to have things ride the trains we need to be able to
        # override "global" things. Therefore, we shouldn't override anything
        # that's already been set.
        if key in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for key, value in BRANCH_UNITTEST_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_UNITTEST_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Copy in local config
    if branch in localconfig.BRANCHES:
        for key, value in localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    # Merge in any project branch config for platforms
    if branch in ACTIVE_PROJECT_BRANCHES and 'mobile_platforms' in PROJECT_BRANCHES[branch]:
        for platform, platform_config in PROJECT_BRANCHES[branch]['mobile_platforms'].items():
            if platform in PLATFORMS:
                for key, value in platform_config.items():
                    value = deepcopy(value)
                    if isinstance(value, str):
                        value = value % locals()
                    BRANCHES[branch]['platforms'][platform][key] = value

    for platform, platform_config in localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

########
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

# Let's load the defaults
for branch in BRANCHES.keys():
    BRANCHES[branch]['repo_path'] = branch
    BRANCHES[branch]['branch_name'] = branch.title()
    BRANCHES[branch]['mobile_branch_name'] = branch.title()
    BRANCHES[branch]['build_branch'] = branch.title()
    BRANCHES[branch]['enable_unittests'] = True
    BRANCHES[branch]['talos_command'] = TALOS_CMD
    BRANCHES[branch]['fetch_symbols'] = True
    BRANCHES[branch]['fetch_release_symbols'] = False
    BRANCHES[branch]['talos_from_source_code'] = True
    BRANCHES[branch]['support_url_base'] = 'http://build.mozilla.org/talos'
    loadTalosSuites(BRANCHES, SUITES, branch)
    BRANCHES[branch]['pgo_strategy'] = None
    BRANCHES[branch]['pgo_platforms'] = []

# The following are exceptions to the defaults

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['mobile_branch_name'] = "Mobile"
BRANCHES['mozilla-central']['mobile_talos_branch'] = "mobile"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['pgo_strategy'] = 'periodic'
BRANCHES['mozilla-central']['pgo_platforms'] = []
BRANCHES['mozilla-central']['platforms']['android']['enable_debug_unittests'] = True

######### mozilla-release
BRANCHES['mozilla-release']['release_tests'] = 1
BRANCHES['mozilla-release']['repo_path'] = "releases/mozilla-release"
BRANCHES['mozilla-release']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-release']['pgo_platforms'] = []

######### mozilla-beta
BRANCHES['mozilla-beta']['release_tests'] = 1
BRANCHES['mozilla-beta']['repo_path'] = "releases/mozilla-beta"
BRANCHES['mozilla-beta']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-beta']['pgo_platforms'] = []

######### mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-aurora']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-aurora']['pgo_platforms'] = []

######### mozilla-esr17
BRANCHES['mozilla-esr17']['release_tests'] = 5
BRANCHES['mozilla-esr17']['repo_path'] = "releases/mozilla-esr17"
BRANCHES['mozilla-esr17']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-esr17']['pgo_platforms'] = []

######### mozilla-b2g18
BRANCHES['mozilla-b2g18']['release_tests'] = 1
BRANCHES['mozilla-b2g18']['repo_path'] = "releases/mozilla-b2g18"
BRANCHES['mozilla-b2g18']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18']['pgo_platforms'] = []

######### mozilla-b2g18_v1_0_0
BRANCHES['mozilla-b2g18_v1_0_0']['release_tests'] = 1
BRANCHES['mozilla-b2g18_v1_0_0']['repo_path'] = "releases/mozilla-b2g18_v1_0_0"
BRANCHES['mozilla-b2g18_v1_0_0']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18_v1_0_0']['pgo_platforms'] = []

######### mozilla-b2g18_v1_0_1
BRANCHES['mozilla-b2g18_v1_0_1']['release_tests'] = 1
BRANCHES['mozilla-b2g18_v1_0_1']['repo_path'] = "releases/mozilla-b2g18_v1_0_1"
BRANCHES['mozilla-b2g18_v1_0_1']['pgo_strategy'] = 'per-checkin'
BRANCHES['mozilla-b2g18_v1_0_1']['pgo_platforms'] = []

######## try
BRANCHES['try']['platforms']['android']['enable_debug_unittests'] = True
BRANCHES['try']['pgo_strategy'] = 'try'
BRANCHES['try']['pgo_platforms'] = []
BRANCHES['try']['enable_try'] = True


#-------------------------------------------------------------------------
# MERGE day - Load reftests small for m-c based branches and exclude them for the rest
#-------------------------------------------------------------------------
for branch in ('mozilla-aurora', 'mozilla-beta', 'mozilla-release'):
    BRANCHES[branch]["platforms"]["android"]["panda_android"]["opt_unittest_suites"] = deepcopy(ANDROID_UNITTEST_DICT["opt_unittest_suites"])
    BRANCHES[branch]["platforms"]["android"]["tegra_android"]["opt_unittest_suites"] = deepcopy(ANDROID_UNITTEST_DICT["opt_unittest_suites"])
#-------------------------------------------------------------------------
# End Load reftests small for m-c based branches and exclude them for the rest
#-------------------------------------------------------------------------


#exclude android builds from running on non-cedar branches on pandas
for branch in BRANCHES.keys():
    if 'android' in BRANCHES[branch]['platforms'] and branch not in ("cedar", "mozilla-central", "try", "mozilla-inbound"):
        del BRANCHES[branch]['platforms']['android']['panda_android']
        BRANCHES[branch]['platforms']['android']['slave_platforms'] = ['tegra_android']

######## generic branch variables for project branches
for projectBranch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[projectBranch]
    loadDefaultValues(BRANCHES, projectBranch, branchConfig)
    loadCustomTalosSuites(BRANCHES, SUITES, projectBranch, branchConfig)


# XXX Bug 789373 hack - add android-noion until we have b2g testing
# Delete all references to android-noion once we have b2g jsreftests not in an emulator.
for branch in BRANCHES:
    if branch not in ('mozilla-central', 'mozilla-inbound', 'mozilla-b2g18',
                      'mozilla-b2g18_v1_0_0', 'mozilla-b2g18_v1_0_1', 'try'
                      ):
        if 'android-noion' in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms']['android-noion']


if __name__ == "__main__":
    import sys
    import pprint

    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = dict(BRANCHES.items())

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)

    for suite in sorted(SUITES):
        out = pprint.pformat(SUITES[suite])
        for l in out.splitlines():
            print '%s: %s' % (suite, l)