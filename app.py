#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 5:36 PM
# @Author  : sunwenjun
# @File    : app.py
# @brief: PyCharm

import streamlit as st
import pandas as pd
import numpy as np

data = {'病理学检测信息-报告时间': ['2019年1月24日'],
        '综合检测-报告时间': ['2019年1月24日;2020年4月12日'],
        '手术记录-手术方式': [
            '保留生育功能的全面分期手术:False;全面分期手术:False;肿瘤细胞减灭术:False;腹腔镜探查术:False;辅助性姑息手术:False'],
        '手术记录-报告时间': ['2020年4月12日'],
        '手术记录-残留病灶': ['是否存在残留病灶:False']}

# 显示表格
st.table(data)
