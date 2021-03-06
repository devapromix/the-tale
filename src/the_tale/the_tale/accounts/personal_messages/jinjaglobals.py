
import smart_imports

smart_imports.all()


@dext_jinja2.jinjaglobal
def sorted_recipients(recipients_ids, accounts):
    recipients = [accounts[recipient_id] for recipient_id in recipients_ids]
    recipients.sort(key=lambda account: account.nick_verbose)
    return recipients


@dext_jinja2.jinjaglobal
def new_messages_number_url():
    return logic.new_messages_number_url()


@dext_jinja2.jinjaglobal
def personal_messages_settings():
    return conf.settings
