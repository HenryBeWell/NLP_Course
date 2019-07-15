"""
知识梳理：
    构建语句生成器的几个步骤：
        1.设定语法规则
            example：
                adj_grammar = "
                    Adj* => null | Adj Adj*
                    Adj =>  蓝色的 | 好看的 | 小小的
                    "
        2.生成语法
            example：
                grammar={'Adj*': [['null'], ['Adj', 'Adj*']],
                        'Adj': [['蓝色的'], ['好看的'], ['小小的']]
                        }
        3.生成句子
            example：

"""
