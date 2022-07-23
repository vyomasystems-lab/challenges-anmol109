# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    for i in range (31):
        dut.inp0.value=0
        dut.inp1.value=0
        dut.inp2.value=0
        dut.inp3.value=0
        dut.inp4.value=0
        dut.inp5.value=0
        dut.inp6.value=0
        dut.inp7.value=0
        dut.inp8.value=0
        dut.inp9.value=0
        dut.inp10.value=0
        dut.inp11.value=0
        dut.inp12.value=0
        dut.inp13.value=0
        dut.inp14.value=0
        dut.inp15.value=0
        dut.inp16.value=0
        dut.inp17.value=0
        dut.inp18.value=0
        dut.inp19.value=0
        dut.inp20.value=0
        dut.inp21.value=0
        dut.inp22.value=0
        dut.inp23.value=0
        dut.inp24.value=0
        dut.inp25.value=0
        dut.inp26.value=0
        dut.inp27.value=0
        dut.inp28.value=0
        dut.inp29.value=0
        dut.inp30.value=0

        A=i
        B=1
        dut.sel.value=i 
        if(i==0):dut.inp0.value=1
        elif(i==1):dut.inp1.value=1
        elif(i==2):dut.inp2.value=1
        elif(i==3):dut.inp3.value=1
        elif(i==4):dut.inp4.value=1
        elif(i==5):dut.inp5.value=1
        elif(i==6):dut.inp6.value=1
        elif(i==7):dut.inp7.value=1
        elif(i==8):dut.inp8.value=1
        elif(i==9):dut.inp9.value=1
        elif(i==10):dut.inp10.value=1
        elif(i==11):dut.inp11.value=1
        elif(i==12):dut.inp12.value=1
        elif(i==13):dut.inp13.value=1
        elif(i==14):dut.inp14.value=1
        elif(i==15):dut.inp15.value=1
        elif(i==16):dut.inp16.value=1
        elif(i==17):dut.inp17.value=1
        elif(i==18):dut.inp18.value=1
        elif(i==19):dut.inp19.value=1
        elif(i==20):dut.inp20.value=1
        elif(i==21):dut.inp21.value=1
        elif(i==22):dut.inp22.value=1
        elif(i==23):dut.inp23.value=1
        elif(i==24):dut.inp24.value=1
        elif(i==25):dut.inp25.value=1
        elif(i==26):dut.inp26.value=1
        elif(i==27):dut.inp27.value=1
        elif(i==28):dut.inp28.value=1
        elif(i==29):dut.inp29.value=1
        elif(i==30):dut.inp30.value=1

        await Timer(2, units='ns')
        assert dut.out.value==1, "Test failed at input:{A}".format(A=dut.sel.value)
        


            
            

        


