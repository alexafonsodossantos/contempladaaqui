<table>
<tr>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<?php
$conexao = mysqli_connect('bd_cotas.mysql.dbaas.com.br','bd_cotas','Ab742853964');
$banco = mysqli_select_db($conexao,'bd_cotas');
mysqli_set_charset($conexao,'utf8');

$sql = mysqli_query($conexao,"select * from TB_COTAS") or die("Erro");
while($dados=mysqli_fetch_assoc($sql))
{
?>
<tr>
<td height="17"><img src="<?php echo $dados['ADMINISTRADORA'] ?>" alt="<?php echo $dados['CARTA'] ?>" width="100"></td>
		<td  valign=middle sdval="45402" sdnum="1033;0;_-&quot;R$ &quot;* #.##0,00_-;-&quot;R$ &quot;* #.##0,00_-;_-&quot;R$ &quot;* &quot;-&quot;??_-;_-@_-"> <?php echo $dados['CREDITO'] ?> </td>
		<td valign=middle sdval="17678.14" sdnum="1033;0;_-&quot;R$ &quot;* #.##0,00_-;-&quot;R$ &quot;* #.##0,00_-;_-&quot;R$ &quot;* &quot;-&quot;??_-;_-@_-"> <?php echo $dados['ENTRADA'] ?> </td>
		<td><?php echo $dados['PARCELAS'] ?></td>
		<td><?php echo $dados['SEGMENTO'] ?></td>
		<td sdnum="1033;1033;M/D/YYYY"><?php echo $dados['VENCIMENTO'] ?></td>
		<td sdval="10611" sdnum="1033;"><?php echo $dados['CODIGO'] ?></td>
		<td sdval="10611" sdnum="1033;"><a href="https://api.whatsapp.com/send?phone=5519989081276&text=Ol%C3%A1%2C%20vi%20o%20seu%20site%20e%20tenho%20interesse%20no%20cr%C3%A9dito%20de%20c%C3%B3digo%<?php echo $dados['CODIGO'] ?>" target="_blank" class="btn btn-success" title="Quero essa cota">Quero essa cota</a></td>
	</tr>
<?php
}
?>
</table>