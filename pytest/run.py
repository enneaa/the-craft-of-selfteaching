from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

divmod(11, 3)
a, b = divmod(11, 3)
a
b


divmod(3, 11)
a, b = divmod(3, 11)
a
b


print(a, b)