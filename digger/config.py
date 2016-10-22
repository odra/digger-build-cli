from addict import Dict


app_folder = '/app'

build_tool_version = '23.0.3'
gradle_plugin = 'apply plugin: \'com.android.application\''
sdk_version = '23'

keystore = Dict()
keystore.path = '/etc/digger/debug.keystore'
keystore.storepass = 'android'
keystore.keypass = 'android'
keystore.alias = 'androiddebug'
