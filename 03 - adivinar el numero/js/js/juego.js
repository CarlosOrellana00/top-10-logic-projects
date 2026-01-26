export function generarSecreto(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

export function evaluarIntento(secreto, intento) {
  if (intento === secreto) return "correcto";
  if (intento > secreto) return "alto";
  return "bajo";
}
