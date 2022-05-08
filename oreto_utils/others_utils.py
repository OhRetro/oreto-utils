#Others

class Others:
    def formatsize(byte_size, return_as:str="unit"):
        if return_as not in ["unit", "number"]:
            raise ValueError("The return_as argument must be 'unit' or 'number'.")

        if byte_size < 1024:
            selected_unit = 0
        elif byte_size < 1024**2:
            selected_unit = 1
        elif byte_size < 1024**3:
            selected_unit = 2
        elif byte_size < 1024**4:
            selected_unit = 3
        elif byte_size < 1024**5:
            selected_unit = 4
        else:
            selected_unit = 5

        if byte_size >= 1024:
            formated_size = float(f"{byte_size/1024**selected_unit:.2f}")
        else:
            formated_size = byte_size

        if return_as == "unit":
            units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
            return f"{formated_size} {units[selected_unit]}"
        elif return_as == "number":
            return formated_size