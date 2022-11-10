# This entity is used to get a dataset from the Data Fair API.


# LIST OF THE FIELDS

# nom_methode_dpe
# version_methode_dpe
# classe_consommation_energie
# classe_estimation_ges
# tr001_modele_dpe_type_libelle
# tr002_type_batiment_description
# code_insee_commune_actualise
# tv016_departement_code
# geo_adresse

import requests as req


class Dataset:

    URL_BASE = "https://koumoul.com/data-fair/api/v1/datasets/dpe-france/"

    def __init__(self, fields="nom_methode_dpe", size=0, select=(), sort=()):
        self.fields = fields
        self.size = size
        self.select = select
        self.sort = sort

    @classmethod
    def getFields(cls):
        """
        Returns a list of fields for which value is desired
        """
        return cls.fields

    @classmethod
    def getSize(cls):
        """
        Return size of the dataset
        """
        return cls.size

    @classmethod
    def getSelect(cls):
        """
        Return the selected filed for the dataset
        """
        return cls.select

    @classmethod
    def getSort(cls):
        """
        Return the sort filed sot this dataset
        """
        return cls.sort

    def getFieldValue(self):
        """
        Return list of value of the field selected
        dependents on the size of the dataset
        Args : 
            fields : field name
            size   : int
        Return:
            json data
        """
        resp = req.get(self.URL_BASE + "values/" + self.fields +
                       "?size=" + str(self.size))
        return resp.json()

    def getData(self):
        """
        Return list of data of the dataset
        dependents on the size of the dataset and the field selected
        Args :
            select : tupple of field name
            sort   : tupple of field name
            size   : int
        Return:
            json data
        """
        try:
            url = self.URL_BASE + "lines"
            if (self.size != 0):
                url = url+"?size="+str(self.size)
            if (len(self.select) != 0):
                url += "&select=" + "%2C".join(self.select)
            if (len(self.sort) != 0):
                url += "&sort=" + "%2C".join(self.sort)

            resp = req.get(url)
            return resp.json()
        except:
            return "An error occured with the API please check your parameters"


t = Dataset(select=("consommation_energie",
            "classe_consommation_energie"), size=2)
print(t.getData())
