#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:03:09 2017

@author: lrh
"""

class DefaultConf(object):
    def __init__(self):
	self.debug = False
        self.batch_size = 256
        self.root_path = "/home/lili/Tao_Zhang/dataset/mnist"
        self.istraining = False
        self.cuda= True
        self.lr = 0.01
        
	self.model_name = "pkls/mnist_capsule_20171124_sgd.pkl_560"
        self.epoch_num = 1000
        
        self.visualize = True
        #visualize train loss
        self.train_loss_env = "mnist_capsule_train20171124"
        self.train_loss_win = None
    
if __name__=="__main__":
    conf = DefaultConf()
    print conf.batch_size
