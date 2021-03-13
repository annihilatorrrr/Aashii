"""
Contains Message object.
"""


class Message:

    """
    Message contains text strings that is used in users interaction.
    """

    ADMIN_CONNECTED = (
        "<a href='tg://user?id={ADMIN_ID}'>{ADMIN_FULL_NAME}</a> "
        "has connected with "
        "<a href='tg://user?id={USER_ID}'>{USER_FULL_NAME}</a>"
    )

    ANNOUNCEMENT_CANCELLED = (
        "Announcement cancelled in progress.\n"
        " • <b>Sent</b> : <code>{SENT}</code>\n"
        " • <b>Failed</b> : <code>{FAILED}</code>\n"
        " • <b>Progress</b> : <code>{PROGRESS}</code>%."
    )

    ANNOUNCEMENT_DONE = (
        "Announcement done.\n"
        " • <b>Sent</b> : <code>{SENT}</code>\n"
        " • <b>Failed</b> : <code>{FAILED}</code>\n"
        " • <b>Total</b> : <code>{TOTAL}</code>."
    )

    ANNOUNCEMENT_IN_DUE = (
        "There is already an announcement in due. "
        "Please /cancel it before starting new one."
    )

    ANNOUNCEMENT_INIT = (
        "An announcement has been initiated.\n"
        "<b>Audience</b> : <code>{TOTAL}</code> users."
    )

    ANNOUNCEMENT_PULSE = (
        "Annoucement in due.\n"
        " • <b>Sent</b> : <code>{SENT}</code>\n"
        " • <b>Failed</b> : <code>{FAILED}</code>\n"
        " • <b>Progress</b> : <code>{PROGRESS}</code>%."
    )

    BLOCKED_USER = "<a href='tg://user?id={USER_ID}'>{FULL_NAME}</a> has been blocked successfully."

    BLOCKED_USER_STATUS = "You are blocked from contacting the admins."

    CANCELLED_ANNOUNCEMENT = (
        "Cancelled announcement at <code>{PROGRESS}</code>% progress."
    )

    HELP_GROUP = (
        "Hey there ! It's <b>Aashii</b> here to help you "
        "in managing communication between members and admins.\n\n"
        "Since you are in <b>admins group</b>, the following commands are your exclusive.\n\n"
        " ⁃ /block - Blocks a user from contacting you.\n"
        " ⁃ /cancel - Cancels a progressing announcement.\n"
        " ⁃ /unblock - Unblocks a blocked user.\n\n"
        "All the above commands should be a reply to a message.\n"
        "For <code>block</code> and <code>unblock</code>, "
        "the replied message should be a forwarded message by me.\n\n"
        "My source code is available at https://github.com/j-arun-mani/Aashii\n"
        "Enjoy !"
    )

    HELP_PRIVATE = (
        "Hey there ! It's <b>Aashii</b> here to help you "
        "in managing communication between members and admins.\n\n"
        "From a <b>member</b> point of view, using me is dead easy.\n"
        "Just send me any message you wish to inform the admins and "
        "I will forward it to them.\n\n"
        "My source code is available at https://github.com/j-arun-mani/Aashii\n"
        "Enjoy !"
    )

    INVALID_COMMAND = "I don't understand what you are talking about ..."

    INVALID_REPLY = "I expected this as a reply to my message."

    NO_ANNOUNCEMENT = "No announcement is in due to cancel."

    NO_USERNAME = "None"

    NOT_LINKED = "I don't think that message corresponds to any user."

    NOT_PRIVATE_COMMAND = "Sorry, this command is meant to be used in admins group."

    START_GROUP = "I'm all alive and functioning."

    START_PRIVATE = (
        "Hello. What do you want to convey the admins of <b>{GROUP_NAME}</b> ?"
    )

    UNBLOCKED_USER = (
        "<a href='tg://user?id={USER_ID}'>{FULL_NAME}</a> has been unblocked."
    )

    UNBLOCKED_USER_STATUS = "You are now allowed to contact the admins."

    USER_CONNECTED = (
        "<a href='tg://user?id={USER_ID}'>{FULL_NAME}</a> has started the bot.\n"
        "Username : {USERNAME}\n"
        "User ID : <code>{USER_ID}</code>\n"
        "Status : {STATUS}."
    )

    USER_NOT_FOUND = "I can't find the user in my database, something's wrong ..."
