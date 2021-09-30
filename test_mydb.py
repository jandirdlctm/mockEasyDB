from mydb import MyDB
import os.path
import pickle

def describe_MyDB():

    def describe_init():

        def it_creates_new_db_file_if_it_does_not_exist(mocker):
            # stub
            mocker.patch("os.path.isfile", return_value=False)
            mocker.patch("pickle.dump")
            f = mocker.patch("builitins.open", mocker.mock_open())
            db = MyDB("test.db")

            os.path.isfile.assert_called_once_with("test.db")
            pickle.dump.assert_called_once_with([], f.return_value)


            # pickle.load
            #fully test saveString

            #test all this methods without allowing dump and load

            