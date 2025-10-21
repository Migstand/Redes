class IPAdress:
    def __init__(self, ipvq, mascara):
        self.__ipvq = self.set_ipvq(ipvq)
        self.__mascara = self.set_mascara(mascara)
        self.__barra = self.numero_da_masca()
    def set_ipvq(self, ipvq):
        a, b, c, d = map(int,ipvq.split("."))
        if (a < 0 or a >255) or (b < 0 or b >255) or (c < 0 or c >255) or (d < 0 or d >255):
            raise ValueError("Informe um ip válido!")
        else: self.ipvq = ipvq

    def set_mascara(self, mascara):
        mascaras_possiveis = [255,254, 252, 248, 240, 224, 192, 128, 0]
        e, f, g, h, = map(int,mascara.split("."))
        if (e in mascaras_possiveis) and (f in mascaras_possiveis) and (g in mascaras_possiveis) and (h in mascaras_possiveis):
            if (e != 255) and (f != 0 or g != 0 or h != 0):
                raise ValueError("Informe uma máscara válida!")
            elif (f != 255) and (g != 0 or h != 0):
                raise ValueError("Informe uma máscara válida!")
            elif (g != 255) and (h != 0):
                raise ValueError("Informe uma máscara válida!")
            else:
                self.mascara = mascara

        
    def get_ipvq(self):
        return self.__ipvq
    def get_mascara(self):
        return self.__mascara
    def get_bara(self):
        return self.__barra
    
    def end_rede(self):
        oipu, oipd, oipt, oipq = map(int, self.__ipvq.split("."))
        omu, omd, omt, omq = map(int, self.__mascara.split("."))
        rede = f"{str(oipu & omu)}.{str(oipd & omd)}.{str(oipt & omt)}.{str(oipq & omq)}"
        return rede
    def end_broadcast(self):
        oipu, oipd, oipt, oipq = map(int, self.__ipvq.split("."))
        omu, omd, omt, omq = map(int, self.__mascara.split("."))
        omu = omu ^ 255
        omd = omd ^ 255
        omt = omt ^ 255
        omq = omq ^ 255
        broadcast = f"{str(oipu | omu)}.{str(oipd | omd)}.{str(oipt | omt)}.{str(oipq | omq)}"
        return broadcast
    def numero_da_masca(self):
        omu, omd, omt, omq = map(int,self.__mascara.split("."))
        m = 0
        for i in range(8):
            m = m + (omu%2)
        for i in range(8):
            m = m + (omd%2)
        for i in range(8):
            m = m + (omt%2)
        for i in range(8):
            m = m + (omq%2)
        self.__barra = m
        return self.__barra

    def pertence_a_rede(self, ip):
        if self.end_rede() == ip or self.end_broadcast() == ip:
            return "Ip não pertence a rede"
        ipu, ipd, ipt, ipq = map(int,ip.split("."))
        oipu, oipd, oipt, oipq = map(int, self.end_rede().split("."))
        omu, omd, omt, omq = map(int, self.end_broadcast().split("."))
        if ((ipq > oipq) and (ipq < omq)) or ((ipq == oipq and ipu == omq)):
            if ((ipt > oipt) and (ipt < omt))or (ipt == oipt and ipt == omt):
                if ((ipd > oipd) and (ipd < omd)) or (ipd == oipd and ipd == omd):
                    if ((ipu > oipu) and (ipu < omu)) or (ipu == oipu and ipu == omu):
                        return "Ip pertence a rede"
                    else: return "Ip não pertence a rede"
                else: return "Ip não pertence a rede"
            else: return "Ip não pertence a rede"
        else: return "Ip não pertence a rede"

    def __str__(self):
            
        return f"{self.__ipvq}/{self.__barra}"

class UI:
    def main():
        ip = IPAdress(input(), input())

        print(ip)
        print(ip.end_rede())                  # "192.168.1.0"
        print(ip.end_broadcast())             # "192.168.1.255"
        print(ip.pertence_a_rede(input()))  # True
        print(ip.pertence_a_rede(input()))   # False

UI.main()