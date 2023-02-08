class A:

    #public data members
    var1=None


    # protected data members
    _var2=None


    # privat data members
    __var3=None



    # constructers

    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3



    # public member function

    def displayPublicMembers(self):
        # access public data members
        print('Public data members :',self.var1)


    def displayProtectMembers(self):
        # accessing protect data members
        print('protect data members:',self._var2)

    def displayPrivatMembers(self):
        # accessing privat data members
        print('privat data members :',self.__var3)



    # public member function
    def accsessPrivatMember(self):
        # acess privat member function
        self.__displayPrivatMembers()


#derived class
class B(A):

    # constructor
    def __init__(self,var1,var2,var3):
        A.__init__(self,var1,var2,var3)


    #publc member function
    def accessProtectMember(self):
        self._displayProtectMembers()


#creating object of derived class
obj=B("pub_re","pro_white","privat_green")

#calling public member function of the class
obj.displayPublicMembers()
obj.accessProtectMember()
obj.accsessPrivatMember()

#obj.accessPrivatMember()
#object can access public members
print('object is accessing public member:',obj.var1)
#object can access protected member
print('object accessing protected memebrs:',obj._var2)

#boject can not access privat member,so it will genarate attribute error
#print(obj.__var3)
print(obj._A__var3)#Accessing name mangled variables
#Name Mangling
#A process in which any given identifier with one trailing underscore and thwo leading underscore
#is textually replaced with _clasName__ifentifier is known as Name mangling
#In _className__identifier name,ClassName is the name of current class where identifier us present