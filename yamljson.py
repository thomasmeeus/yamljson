import sublime
import sublime_plugin
import json

try:
    from . import yaml
except (ImportError, ValueError):
    import yaml

class ConvertYamlToJson(sublime_plugin.TextCommand):
    def run(self, edit):
        sel_view = self.view.sel()
        for region in sel_view:
            if not region.empty():
                input = yaml.load(self.view.substr(region))
                self.view.replace(edit, region, json.dumps(input, sort_keys=True, indent=2))

class ConvertJsonToYaml(sublime_plugin.TextCommand):
    def run(self, edit):
        sel_view = self.view.sel()
        for region in sel_view:
            if not region.empty():
                input = yaml.load(self.view.substr(region))
                self.view.replace(edit, region, yaml.dump(input, allow_unicode=True,default_flow_style=False))