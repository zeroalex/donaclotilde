from donaclotilde import *

class Exemplo(Donaclotilde):
    def __init__(self,):
        self.entrada_select=[]
        self.entrada_from_table=[]
        self.entrada_where=[]
        self.entrada_insert=[]
        self.query=[]


    def list_all(self):
        self.select("*")
        self.from_table("autorizacao_debito")
        sql=self.get()
        dados = self.result_list(sql)
        return dados
    def list_filt(self, search=None ):

        self.select("id")
        self.select("permissionario")

        self.from_table("autorizacao_debito")
        
        if not search is None:
            self.where(search, 'permissionario')
        
        sql=self.get()
        dados = self.result_list(sql)
        return dados