'''
The MIT License (MIT)

Copyright (c) 2015 Patrick Olsen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Patrick Olsen
'''
import sys, imp
import argparse
from PluginManager import SLARFPluginManager

def main():    
    parser = argparse.ArgumentParser(description='Parses SQLite Databases.')
    parser.add_argument('--plugin', required=False,
                        help='Specify plugin to run.')
    parser.add_argument('--listplugins', required=False, 
                        action='store_true', 
                        help='Lists all of the available plugins.')
    parser.add_argument('--plugindetails', required=False, 
                        action='store_true', 
                        help='Lists details available plugins.') 
    parser.add_argument('--database', required=False, 
                        help='SQLite Database.')      
    parser.add_argument('--format', action="store", metavar="format",
                        nargs=1, dest="format",
                        help="Custom output.")
    parser.add_argument('--format_file', action="store", metavar="format_file",
                        nargs=1, dest="format_file",
                        help="Custom output template.")
    args = parser.parse_args()
    
    plugin_directory = "plugins/"

    if args.listplugins:
        SLARFPluginManager().listPlugin(plugin_directory)
    
    elif args.plugindetails:
        SLARFPluginManager().detailedPlugin(plugin_directory)
    
    elif args.plugin is not None:
        found_plugin = SLARFPluginManager().findPlugin(plugin_directory, args.plugin)
        activated_plugin = SLARFPluginManager().loadPlugin(args.plugin, found_plugin)
        
        activated_plugin.PluginClass(args.database, args.format, args.format_file).ProcessPlugin()

    else:
        exit(0)

if __name__ == "__main__":
    main()