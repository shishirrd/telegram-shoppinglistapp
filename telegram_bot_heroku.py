#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import telebot
import sys


# In[2]:


import os
PORT = int(os.environ.get('PORT',5000))


# In[ ]:


API_KEY = '2077563577:AAFruWz-P4oxbCHFPC1ptUlvjMjaYausaZw'


# In[ ]:


bot = telebot.TeleBot(API_KEY)


# In[ ]:


#Define initial shopping list
shopping_list = ['Apples','Bananas','Pears','Carrots','Potatoes']


# In[ ]:


import telegram.ext


# In[ ]:


updater = telegram.ext.Updater(API_KEY, use_context=True)


# In[ ]:


disp = updater.dispatcher


# In[ ]:


def hello(update, context):
    update.message.reply_text("Hello folks! Welcome to Shishir's shopping list bot!. Click on /start to get started!")


# In[ ]:


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


# In[ ]:


def viewList(update, context):
    update.message.reply_text("Here's your list!") 
    update.message.reply_text(str(shopping_list))


# In[ ]:


def addList(update, context):
    item = context.args[0]
    shopping_list.append(item)
    update.message.reply_text(f"{item} has been added to the list!")


# In[ ]:


def removeList(update, context):
    item = context.args[0]
    shopping_list.remove(item)
    update.message.reply_text(f"{item} has been removed from the list!")


# In[ ]:


#Define function for checking whether item is on list
def checkItem(update, context):
    item = context.args[0] 
    if item in shopping_list:
        update.message.reply_text(f"Yes. {item} is on the list!")
    else:
        update.message.reply_text(f"No. {item} is not on the list! Would you like to add this?")


# In[ ]:


#Define function for counting no. of items on list
def listLength(update, context):
    count = len(shopping_list)
    if count > 0:
        update.message.reply_text(f"There are {count} items on the shopping list")
    else:
        update.message.reply_text("There are no items on the shopping list!")


# In[ ]:


#Define function to clear shopping list and start over afresh
def clearList(update, context):
    shopping_list.clear()
    update.message.reply_text("Shopping list is now empty!")


# In[ ]:


disp.add_handler(telegram.ext.CommandHandler("hello", hello))
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("List", viewList))
disp.add_handler(telegram.ext.CommandHandler("Add", addList))
disp.add_handler(telegram.ext.CommandHandler("Remove", removeList))
disp.add_handler(telegram.ext.CommandHandler("Check", checkItem))
disp.add_handler(telegram.ext.CommandHandler("Count", listLength))
disp.add_handler(telegram.ext.CommandHandler("Clear", clearList))


# In[ ]:


updater.start_webhook(listen="0.0.0.0", port = int(PORT), url_path = API_KEY)
updater.bot.setWebhook('https://shishir-telegram-shoppinglist.herokuapp.com/' + API_KEY)
updater.idle()

