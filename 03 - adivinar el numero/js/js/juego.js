export function generarSecreto(min, max){
  //Math.random() -> numero entre 0 y 1, sin incluir el 1
  //lo escalamos a  [min, max] y lo redondeamos a entero
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

export function evaluarIntento(secreto, intento){
  if(intento === secreto) return "correcto";
  if(intento > secreto) return "alto";
  return bajo;
}