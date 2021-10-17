#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
PORT = int(os.environ.get('PORT',8443))


# In[2]:


API_KEY = '2077563577:AAFruWz-P4oxbCHFPC1ptUlvjMjaYausaZw'


# import telebot

# bot = telebot.TeleBot(API_KEY)

# def webhook(request):
#     bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
#     if request.method == "POST":
#         update = telegram.Update.de_json(request.get_json(force=True), bot)
#         chat_id = update.message.chat.id
#         # Reply with the same message
#         bot.sendMessage(chat_id=chat_id, text=update.message.text)
#     return "ok"
#     return "error"

# def index():
#     return webhook

# In[3]:


#Define initial shopping list
shopping_list = ['Apples','Bananas','Pears','Carrots','Potatoes']


# In[4]:


import telegram.ext


# In[5]:


updater = telegram.ext.Updater(API_KEY, use_context=True)


# In[6]:


disp = updater.dispatcher


# In[7]:


def hello(update, context):
    update.message.reply_text("Hello folks! Welcome to Shishir's shopping list bot!. Click on /start to get started!")


# In[8]:


def main():
    #Define main menu for user to see when they first access the bot
    def start(update, context):
        #Print a menu for a user
        update.message.reply_text("""Select an option for the action that you would like to do:
1. Type /List to view shopping list
2. Add item to list by typing '/Add' followed by the name of the item. Use '_' instead of space
3. Remove item from list by typing '/Remove' followed by the name of the item. Use '_' instead of space
4. Check if item is on the list by typing '/Check' followed by the name of the item. Use '_' instead of space
5. Type /Count to check no. of items are on my list?
6. Type /Clear to clear shopping list""")
        
    def viewList(update, context):
        update.message.reply_text("Here's your list!")
        update.message.reply_text(str(shopping_list))
        
    def addList(update, context):
        item = context.args[0]
        shopping_list.append(item)
        update.message.reply_text(f"{item} has been added to the list!")
        
    def removeList(update, context):
        item = context.args[0]
        shopping_list.remove(item)
        update.message.reply_text(f"{item} has been removed from the list!")
        
    #Define function for checking whether item is on list
    def checkItem(update, context):
        item = context.args[0] 
        if item in shopping_list:
            update.message.reply_text(f"Yes. {item} is on the list!")
        else:
            update.message.reply_text(f"No. {item} is not on the list! Would you like to add this?")
            
   #Define function for counting no. of items on list
    def listLength(update, context):
        count = len(shopping_list)
        if count > 0:
            update.message.reply_text(f"There are {count} items on the shopping list")
        else:
            update.message.reply_text("There are no items on the shopping list!")
    
    #Define function to clear shopping list and start over afresh
    def clearList(update, context):
        shopping_list.clear()
        update.message.reply_text("Shopping list is now empty!")
    
    disp.add_handler(telegram.ext.CommandHandler("hello", hello))
    disp.add_handler(telegram.ext.CommandHandler("start", start))
    disp.add_handler(telegram.ext.CommandHandler("List", viewList))
    disp.add_handler(telegram.ext.CommandHandler("Add", addList))
    disp.add_handler(telegram.ext.CommandHandler("Remove", removeList))
    disp.add_handler(telegram.ext.CommandHandler("Check", checkItem))
    disp.add_handler(telegram.ext.CommandHandler("Count", listLength))
    disp.add_handler(telegram.ext.CommandHandler("Clear", clearList))
    
    updater.start_webhook(listen="0.0.0.0", port = int(PORT), url_path = API_KEY, 
                          webhook_url='https://shishir-telegram-shoppinglist.herokuapp.com/' + API_KEY)
    updater.idle()


# In[ ]:


if __name__ == '__main__':
    main()

