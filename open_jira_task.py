import sublime
import sublime_plugin
import webbrowser
import re
import subprocess
import os


class OpenJiraTask(sublime_plugin.TextCommand):
    def check_config(self):
        settings = self.view.settings()
        if not settings.get('jira_url') or not settings.get('jira_task_regexp'):
            raise Exception('Please Config Jira Url and Task Regexp on Config')

    def get_project_path(self):
        return sublime.active_window().folders()[0]

    def get_branch_name(self):
        try:
            branch_name = subprocess.check_output(['git', '-C', self.get_project_path(), 'rev-parse', '--abbrev-ref', 'HEAD'])
            return branch_name.decode('utf-8').strip()
        except subprocess.CalledProcessError:
            raise Exception('Failed to retrieve Git branch name.')

    def get_task_id(self, branch_name):
        jira_task_regexp = self.view.settings().get('jira_task_regexp')
        matches = re.findall(jira_task_regexp, branch_name)
        if matches:
            return matches[0]
        else:
            raise Exception('No Task ID found.')

    def run(self, edit):
        try:
            self.check_config()
            jira_url = self.view.settings().get('jira_url')
            branch_name = self.get_branch_name()
            task_id = self.get_task_id(branch_name)
            url = '{}/browse/{}'.format(jira_url, task_id)
            print("Open Jira Task:", url)
            webbrowser.open_new_tab(url)
        except Exception as e:
            sublime.status_message('Open Jira Task: {}'.format(e))
