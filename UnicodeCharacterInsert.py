import sublime
import sublime_plugin
import os


class UnicodeCharacterInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        content = self.get_popup_content()
        self.view.show_popup(content, sublime.HTML, location=-1, max_height=640, on_navigate=self.on_choice_symbol)

    def get_popup_content(self):
        tpl_path = os.path.dirname(os.path.realpath(__file__)) + '/unicode-characters.html'
        content = open(tpl_path, 'r').read()
        return content

    def on_choice_symbol(self, symbol):
        self.view.run_command("insert", {"characters": symbol})
        self.view.hide_popup()
