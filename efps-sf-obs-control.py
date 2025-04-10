import obspython as obs
import urllib.request
import urllib.error
import json

sftoken = ''
sfurl = 'https://motd.hl2dm.xyz:25443/'
sfonlineserversurl = 'api/srcds/onlineServers?token='
sfstreamoverlayurl = 'streamerOverlay/?guid='
center = 0
delay = 0
settings = None

def load_servers(prop):
	global sftoken
	global sfurl
	global sfonlineserversurl
	url = f"{sfurl}{sfonlineserversurl}{sftoken}"
	
	try:
		response = urllib.request.urlopen(url)
		if response.status != '200':
			data = response.read()
			onlineservers = json.loads(data.decode('utf-8'))
			obs.obs_property_list_clear(prop)
			for server in onlineservers:
				obs.obs_property_list_add_string(prop, server["name"], server["sessionId"])
		else:
			raise Exception(f"SF Server returned back the following error code: {response.status}")
	except Exception as e:
		obs.script_log(400, f"Something went wrong while looking up the servers: {e}, {sftoken}")

def update_overlay(props, prop):
	global settings
	global sftoken
	global sfurl
	global sfstreamoverlayurl
	global center
	global delay

	sftoken = obs.obs_data_get_string(settings, "SFToken")
	sourcename = obs.obs_data_get_string(settings,"source")
	center = obs.obs_data_get_bool(settings, "center")
	delay = obs.obs_data_get_int(settings, "delay")
	selectedguid = obs.obs_data_get_string(settings,"SFServerList")
	
	
    # Get the current Overlay Source.
	source = obs.obs_get_source_by_name(sourcename)
	source_settings = obs.obs_source_get_settings(source)
	data = json.loads(obs.obs_data_get_json(source_settings))
	newurl = f"{sfurl}{sfstreamoverlayurl}{selectedguid}&token={sftoken}&center={int(center)}&delay={delay}"
	
	if data["url"] != newurl:
		print(f"Updating to: {selectedguid} with center set to {int(center)} and delay set to {delay}")
		obs.obs_data_set_string(source_settings, "url", newurl)
		obs.obs_source_update(source, source_settings)

    
	obs.obs_data_release(source_settings)
	obs.obs_source_release(source)

def load_servers_pressed(props, prop):
	serverlist = obs.obs_properties_get(props, 'SFServerList')
	load_servers(serverlist)
	return True

def script_description():
	return "Attempts to give user control over SF Player Overlay Config. \n\n by SirEdges"

def script_properties():
	props = obs.obs_properties_create()
	obs.obs_properties_add_text(props, 'SFToken', 'Enter your SF Token here for api usage.', obs.OBS_TEXT_PASSWORD)
	p = obs.obs_properties_add_list(props, "source", "Overlay Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
	sources = obs.obs_enum_sources()
	if sources is not None:
		for source in sources:
			source_id = obs.obs_source_get_unversioned_id(source)
			if source_id == "browser_source":
				name = obs.obs_source_get_name(source)
				obs.obs_property_list_add_string(p, name, name)
		obs.source_list_release(sources)
	obs.obs_properties_add_bool(props, 'center', 'Center Overlay?')
	obs.obs_properties_add_int(props, 'delay', 'Delay (seconds)', 0, 360, 1)
	serverlist = obs.obs_properties_add_list(props, 'SFServerList', 'Select which server to load from.', obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
	obs.obs_properties_add_button(props, 'Load Servers', 'Load server list', load_servers_pressed)
	obs.obs_properties_add_button(props, 'UpdateOverlay', 'Update Overlay', update_overlay)
	return props

def script_update(new_settings):
	global settings
	settings = new_settings

	global sftoken
	global sfurl
	global sfstreamoverlayurl
	global center
	global delay

	sftoken = obs.obs_data_get_string(settings, "SFToken")
	center = obs.obs_data_get_bool(settings, "center")
	delay = obs.obs_data_get_int(settings, "delay")
	

def script_load(settings):
	return True