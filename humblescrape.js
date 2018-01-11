function Scrape()
{
  $data = getData()
  saveData($data, "output.txt")
}

function getData()
{
  $data = ''
  $library = document.querySelector(".subproducts-holder")
  for (var i=0, len=$library.childElementCount; i < len; i++)
  {
    console.log(i)
    $library.childNodes[i].click()
    $details = document.querySelector(".details-view")
    $data += "--------------------------\r\nItem " + i + "\n--------------------------\r\n"
    for (var j = 0, lenj = $details.childElementCount; j < lenj; j++)
    {
      $data += $details.children[j].innerText + "\n"
    }
    $data += "\r\n"
  }
  return $data
}

function saveData(data, fileName)
{
    var a = document.createElement("a");
    var blob = new Blob([$data], {type: 'text/plain'})
    document.body.appendChild(a);
    a.style = "display: none";
    url = window.URL.createObjectURL(blob);
    a.href = url;
    a.download = fileName;
    a.click();
    window.URL.revokeObjectURL(url);
}

