"""
By: Drew Reid
Date: May 2, 2015
Purpose: 
    class to parse the Config File
"""

from configparser import ConfigParser

class DatabasePostgresConfig:


    _parser = None
    
    def __init__(self, configure_file):
        self._parser = ConfigParser()
        self._parser.read(configure_file)
    
    #read the databse connection details
    def ReadDatabaseConnection(self, section='dbPostgres'):
        db = {}
        if self._parser.has_section(section):
            items = self._parser.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise Exception("{0} not found in the {1} file" \
                            .format(section, self.file))
        return db
    
    #read the path to the databse upload file
    def ReadDatabasePath(self, section='dbPath'):
        if self._parser.has_section(section):
            return self._parser.get(section, 'path')
        else:
            raise Exception("{0} not found in the {1} file" \
                            .format(section, self.file))
    
    #get the database upload file name
    def ReadDatabaseFile(self, section='dbPath'):
        if self._parser.has_section(section):
            return self._parser.get(section, 'file')
        else:
            raise Exception("{0} not found in the {1} file" \
                            .format(section, self.file))