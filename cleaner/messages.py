message_classes = {
    ("pagination", "block_link"),
    ("message", "default", "clearfix"),
    ("message", "default", "clearfix", "joined"),
    ("message", "service"),
}

joined_classes = {
    "message service",
    "clearfix default message",
    "clearfix default joined message",
    "block_link pagination",
}

# "block_link pagination" and "message service" are useless to me

# Encountered message.body.children classes
message_body_children = [
    ('bot_buttons_table', 'date details pull_right', 'from_name', 'text'),
    ('bot_buttons_table', 'date details pull_right', 'details reply_to', 'from_name', 'text'),
    ('bot_buttons_table', 'clearfix media_wrap', 'date details pull_right', 'from_name'),
    ('bot_buttons_table', 'clearfix media_wrap', 'date details pull_right', 'from_name', 'text'),
    ('bot_buttons_table', 'clearfix media_wrap', 'date details pull_right', 'details reply_to', 'from_name'),
    ('bot_buttons_table', 'clearfix media_wrap', 'date details pull_right', 'details reply_to', 'from_name', 'reactions'), 

    ('body forwarded', 'date details pull_right', 'forwarded pull_left userpic_wrap', 'from_name'),
    ('body forwarded', 'date details pull_right', 'forwarded pull_left userpic_wrap', 'from_name', 'reactions'),

    ('date details pull_right', 'from_name'),
    ('date details pull_right', 'from_name', 'text'),
    ('date details pull_right', 'from_name', 'reactions', 'text'),

    ('date details pull_right', 'details reply_to', 'from_name'),
    ('date details pull_right', 'details reply_to', 'from_name', 'text'),
    ('date details pull_right', 'details reply_to', 'from_name', 'reactions', 'text'),

    ('clearfix media_wrap', 'date details pull_right', 'from_name'),
    ('clearfix media_wrap', 'date details pull_right', 'from_name', 'text'),
    ('clearfix media_wrap', 'date details pull_right', 'from_name', 'reactions'),
    ('clearfix media_wrap', 'date details pull_right', 'from_name', 'reactions', 'text'),

    ('clearfix media_wrap', 'date details pull_right', 'details reply_to', 'from_name'),
    ('clearfix media_wrap', 'date details pull_right', 'details reply_to', 'from_name', 'reactions'),
    ('clearfix media_wrap', 'date details pull_right', 'details reply_to', 'from_name', 'text'),
    ('clearfix media_wrap', 'date details pull_right', 'details reply_to', 'from_name', 'reactions', 'text'),
]