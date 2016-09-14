#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import hug


deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
# 只需要训练一次，不需要每次启动进程都训练，训练结果默认存到本地`./database.db`,之后启动进程会使用这个数据库
deepThought.train("chatterbot.corpus.chinese")  # 语料库
deepThought.train("chatterbot.corpus.english")  # 语料库
deepThought.train("chatterbot.corpus.chinese.greetings")  # 语料库
deepThought.train("chatterbot.corpus.english.greetings")  # 语料库
deepThought.train("chatterbot.corpus.chinese.conversations")  # 语料库
deepThought.train("chatterbot.corpus.english.conversations")  # 语料库
deepThought.train("chatterbot.corpus.chinese.trivia")  # 语料库


@hug.get()
def get_response(user_input):
    response = deepThought.get_response(user_input).text
    return {"response":response}
