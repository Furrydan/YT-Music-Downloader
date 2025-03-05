def correct(title):
        title = title.replace('/', '-')
        title = title.replace('\\', '-')
        title = title.replace('?', '-')
        title = title.replace(':', '-')
        title = title.replace('<', '-')
        title = title.replace('>', '-')
        title = title.replace('*', '-')
        title = title.replace('"', '-')
        title = title.replace('|', '-')
        return title