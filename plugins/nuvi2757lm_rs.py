import sys
from PluginManager import SLARFPluginManager
from jinja2 import Template, Environment, PackageLoader

class PluginClass(object):

    def __init__(self, database=None, format=None, format_file=None):
        self.database = database
        self.format = format
        self.format_file = format_file
    
    def ProcessPlugin(self):
        env = Environment(keep_trailing_newline=True, loader=PackageLoader('slarf', 'templates'))
        results = []
        
        (conn, cursor) = SLARFPluginManager().get_conn_cursor(self.database)
        cursor.execute("SELECT rank, string FROM searches")
        row = cursor.fetchone()
        while row is not None:
            results.append((row[0], row[1]))
            row = cursor.fetchone()
        
        if self.format is not None:
            for entry in results:
                rank = entry[0]
                string = entry[1]
                template = Environment().from_string(self.format[0])
                sys.stdout.write(template.render(rank=rank, string=string) + "\n")
                
        elif self.format_file is not None:
            with open(self.format_file[0], "rb") as f:
                template = env.from_string(f.read())
                sys.stdout.write(template.render(results=results))