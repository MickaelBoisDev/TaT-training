from invoke import task

@task
def show_code_report(c, app_name):
    print('Showing code report for app {}'.format(app_name))
    c.run('autopep8 -d --aggressive -r {}'.format(app_name))


@task
def fix_code_format(c, app_name):
    print('Fixing code for app {}'.format(app_name))
    c.run('autopep8 -i --aggressive -r {}'.format(app_name))
    print('Code fixed')


@task
def format_app_code(c, app_name):
    show_code_report(c, app_name)
    confirm = input('Would you like to fix the code of the app automatically ? [yes/no]')
    if (confirm == 'yes' or confirm == 'y'):
        fix_code_format(c, app_name)
