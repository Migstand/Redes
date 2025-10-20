class IPAdress:
    def __init__(self, ipvq, mascara):
        self.ipvq = ipvq
        self.mascara = mascara
    def set_ipvq(self, ipvq):
        a, b, c, d = int(ipvq.split("."))
        if (a < 0 or a >255) or (b < 0 or b >255) or (c < 0 or c >255) or (d < 0 or d >255):
            raise ValueError("Informe um ip válido!")
        else: self.ipv4 = ipv4
        self.ipv4 = ipv4

    def set_mascara(self, mascara):
        mascaras_possiveis = [255,254, 252, 248, 240, 224, 192, 128, 0]
        e, f, g, h, = int(mascara.split("."))
        if (e in mascaras_possiveis) and (f in mascaras_possiveis) and (g in mascaras_possiveis) and (h in mascaras_possiveis):
            self.mascara = mascara
        else: raise ValueError("Informe uma máscara válida!")
        
    def get_ipvq(self):
        return self.ipvq
    def get_mascara(self):
        return self.mascara
    
    def end_rede(self):
        oipu, oipd, oipt, oipq = map(int, self.ipvq.split("."))
        omu, omd, omt, omq = map(int, self.mascara.split("."))
        rede = f"{str(oipu & omu)}.{str(oipd & omd)}.{str(oipt & omt)}.{str(oipq & omq)}"
        return rede
    def end_broadcast(self):
        oipu, oipd, oipt, oipq = map(int, self.ipvq.split("."))
        omu, omd, omt, omq = map(int, self.mascara.split("."))
        omu = ~(omu)
        omd = ~(omd)
        omt = ~(omt)
        omq = ~(omq)
        broadcast = f"{str(oipu | omu)}.{str(oipd | omd)}.{str(oipt | omt)}.{str(oipq | omq)}"
        return broadcast

    def pertence_a_rede(self, ip):
        ipu, ipd, ipt, ipq = ip.split(".")
        oipu, oipd, oipt, oipq = (self.ipvq.split("."))
        omu, omd, omt, omq = (self.mascara.split("."))
        bip = int(ipu + ipd + ipt + ipq)
        bipvq = int(oipu + oipd + oipt + oipq)
        bom = int(omu + omd + omt + omq)
        if (bip > bipvq) and (bip < bom):
            return "Ip pertence a rede"
        else: 
            return "Ip não pertence a rede"

    def __str__(self):
        
        omu, omd, omt, omq = map(int,self.mascara.split("."))
        omu = str(bin(omu))
        return omu
        omd = str(bin(omd))
        omt = str(bin(omt))
        omq = str(bin(omq))
        m = 0
        # for i in range(8):
        #     m = m + int(omu[i])
        # for i in range(8):
        #     m = m + int(omu[i])
        # for i in range(8):
        #     m = m + int(omu[i])
        # for i in range(8):
        #     m = m + int(omu[i])    
        return f"{self.ipvq}/{m}"

class UI:
    def main():
        ip = IPAdress("192.168.1.10", "255.255.255.0")

        print(ip)
        print(ip.end_rede())                  # "192.168.1.0"
        print(ip.end_broadcast())             # "192.168.1.255"
        print(ip.pertence_a_rede("192.168.1.55"))  # True
        print(ip.pertence_a_rede("192.168.2.1"))   # False

UI.main()