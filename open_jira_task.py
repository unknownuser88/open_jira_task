import sublime
import sublime_plugin
import webbrowser
import re
import subprocess
import os


class OpenJiraTask(sublime_plugin.TextCommand):
    def get_project_path(self):
        return sublime.active_window().folders()[0]

    def get_branch_name(self):
        try:
            project_path = self.get_project_path()
            branch_name = subprocess.check_output(['git', '-C', project_path, 'rev-parse', '--abbrev-ref', 'HEAD']).decode('utf-8').strip()
            return branch_name
        except subprocess.CalledProcessError:
            sublime.status_message('Open Jira Task: Failed to retrieve Git branch name.')

    def get_task_id(self, branch_name):
        jira_task_regexp = self.view.settings().get('jira_task_regexp')
        matches = re.findall(jira_task_regexp, branch_name)
        if matches:
            return matches[0]
        else:
            sublime.status_message('Open Jira Task: No matches found.')

    def run(self, edit):
        jira_url = self.view.settings().get('jira_url')
        branch_name = self.get_branch_name()
        task_id = self.get_task_id(branch_name)
        url = '{}/browse/{}'.format(jira_url, task_id)
        print("Open Jira Task:", url)
        webbrowser.open_new_tab(url)
