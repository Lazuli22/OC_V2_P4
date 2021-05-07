from views.view import View


class Form(View):
    """ Abstract class to defines forms of Chess Tournament"""

    def __init__(self):
        pass

    def show(self, titre, options):
        dict_data = {}
        print(titre)
        for k, option in enumerate(options, start=1):
            print(f"{k} - {option}")
            value = input()
            dict_data[f"{option}"] = value
        return dict_data
