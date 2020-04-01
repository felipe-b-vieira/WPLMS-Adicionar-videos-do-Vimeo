# WPLMS-Adicionar-videos-do-Vimeo
Código feito em wordpress usando rest api para poder adicionar vídeos do vímeo a partir de um csv.

Para utilizar é necessário ativar o API point para as units do WPLMS e adicionar os meta do vibe_types e vibe_durations simplesmente adicionando o código presente no txt no functions.php

Também é necessário gerar uma senha de api point através de plugin.<br>
Usei: Application Passwords<br>
A primeira linha do arquivo contendo as aulas deve conter:

usuario,senhaapi,link do api endpoint do wordpress,id do autor,id curso
<br>
Precisa adicionar:<br>
RewriteCond %{HTTP:Authorization} ^(.)<br>
RewriteRule ^(.) - [E=HTTP_AUTHORIZATION:%1]<br>
<br>
//ATUALIZAÇÃO//

No plugin do WP Rest API Controller, alterar no arquivo classs-wp-rest-api-controller.php na pasta includes, mudar a função append_post_type_meta_data_to_api com o código abaixo:<br>
'update_callback' => null,  com:<br>
'update_callback' => 'update_post_meta_for_api',<br>
Adicionar a função no php:<br>
function update_post_meta_for_api( $value, $object, $field_name ) {
<br>
if ( ! $value ) {<br>
    return;<br>
}<br>
<br>
return update_post_meta( $object->ID, $field_name, $value );<br>
}
<br><br>
Além disso, ativar no plugin, o controle de curriculo e vibe_course_curriculum
