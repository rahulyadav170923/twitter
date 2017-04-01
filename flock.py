# from pyflock import FlockClient, verify_event_token
# from pyflock import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction

# flock_client = FlockClient(token="6172ac12-b495-4524-aaa2-e76245cb0d45", app_id="100d8ebf-117a-47cb-ac96-46d202c1e80c")
# userid = 'g:b48c8a547a3f4852afd02a94739823a9'
# send_as_hal = SendAs(name='Flock Support', profile_image='https://pbs.twimg.com/profile_images/1788506913/HAL-MC2_400x400.png')


#  def send_tweet(tweetdata):
#     views = Views()
#     widget = WidgetView(src=,height=250)
#     views.add_widget(widget)
#     b1 = Button(name = "Retweet", id="retweet", action=OpenBrowserAction(url=, send_context=True))
#     b2 = Button(name = "Reply", id="reply", action=OpenBrowserAction(url=, send_context=True))
#     attachment = Attachment(views=views, buttons=[b1,b2])
#     widget_message = Message(to=,text=,attachments = [attachment],send_as=send_as_hal)
#     res = flock_client.send_chat(widget_message)
#     print(res)

# def send_tweet():
#     pass