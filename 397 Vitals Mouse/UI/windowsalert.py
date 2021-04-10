import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom
import sys
import datetime

def sendNotifH():
    #create notifier. find app name by using sys

    nManager = notifications.ToastNotificationManager

    notifier = nManager.create_toast_notifier(sys.executable);

    #define your notification as string
    tString = """
    <toast>
        <visual>
            <binding template='ToastGeneric'>
                <text>High heartrate detected</text>
                <text>Try taking a breather</text>
            </binding>
        </visual>
    </toast>
    """

    #convert notification to an XmlDocument
    xDoc = dom.XmlDocument()
    xDoc.load_xml(tString)

    #display notification
    notifier.show(notifications.ToastNotification(xDoc))

def sendNotifO():
    #create notifier. find app name by using sys

    print(start)
    nManager = notifications.ToastNotificationManager

    notifier = nManager.create_toast_notifier(sys.executable);

    #define your notification as string
    tString = """
    <toast>
        <visual>
            <binding template='ToastGeneric'>
                <text>Low oxygen level detected</text>
                <text>Try taking a breather</text>
            </binding>
        </visual>
    </toast>
    """

    #convert notification to an XmlDocument
    xDoc = dom.XmlDocument()
    xDoc.load_xml(tString)

    #display notification
    notifier.show(notifications.ToastNotification(xDoc))



if __name__ == "__main__":
    sendNotifH()
    sendNotifO()
