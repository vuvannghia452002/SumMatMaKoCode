from unidecode import unidecode


class Convert():
    def LoaiBoDau(input):
        output = unidecode(input).split()
        output = ' '.join(output)
        return output

    def VietHoaTatCa(input):
        output = [word.upper() for word in input]
        output = ''.join(output)
        return output

    def VietThuongTatCa(input):
        output = [word.lower() for word in input]
        output = ''.join(output)
        return output

    def VietHoaDauDongGiuDinhDang(input):
        output = input[0].upper()+input[1:]
        output = ''.join(output)
        return output

    def VietHoaDauDongVaVietThuongConLai(input):
        output = input[0].upper()+input[1:].lower()
        output = ''.join(output)
        return output

    def VarCONST(input):
        words = unidecode(input).split()
        output = [word.upper() for word in words]
        output = '_'.join(output)
        return output

    def VarSnakeCase(input):
        words = unidecode(input).split()
        output = [word.lower() for word in words]
        output = '_'.join(output)
        return output

    def VarCamelCase(input):
        words = unidecode(input).split()
        output = [word.capitalize() for word in words]
        output = ''.join(output)
        output = output[0].lower()+output[1:]
        return output

    def VarPascalCase(input):
        words = unidecode(input).split()
        output = [word.capitalize() for word in words]
        output = ''.join(output)
        return output
