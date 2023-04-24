    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        new_list = args.split()
        if new_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[new_list[0]]()
        for arg_pair in new_list[1:]:
            items_in_list = arg_pair.split("=", 1)
            value = arg_pair[1]
            new_dict = dict(items_in_list)
            print(new_dict)
            setattr(new_instance, arg_pair[0], value)
        new_instance.save()
        print(f"{new_instance.id}")


    


    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        my_list = args.split(" ")
        if my_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[my_list[0]]()
        for arg_pair in my_list[1:]:
            arg_pair = arg_pair.split('=', 1)
            value = arg_pair[1]
            if arg_pair[1][0] == '"':
                value = value[1:-1].replace('_', ' ')
            else:
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
            setattr(new_instance, arg_pair[0], value)
        new_instance.save()
        print(f"{new_instance.id}")

