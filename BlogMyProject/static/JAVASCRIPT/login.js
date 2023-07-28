function validate_Password()
{
  var ps1=document.frm.CreatePassword.value;
  var ps2=document.frm.RetypePassword.value;

  if(ps1==ps2)
  {
    return true;
  }
  else {
    alert("Password must be same!!!");
    return false;
  }
}
