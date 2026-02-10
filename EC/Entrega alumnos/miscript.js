/**
 * Datos de entrada: Array de productos serializados (Simulando una fuente externa)
 * Formato: "IDProducto;Nombre;Precio;Descripción;URL_Imagen"
 */
const arrayProductos = [
  "123;Monitor UltraWide;349.99;Monitor curvo de 34 pulgadas ideal para programar.;https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500",
  "245;Teclado Mecánico;120.50;Teclado RGB con switches blue para una escritura táctil.;https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500",
  "367;Ratón Ergonómico;55.00;Ratón inalámbrico diseñado para largas jornadas de trabajo.;https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500",
  "423;Auriculares Studio;89.00;Cancelación de ruido activa y sonido de alta fidelidad.;https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
  "518;Silla Gaming;199.00;Comodidad extrema para tus sesiones de código.;https://www.powerplanetonline.com/cdnassets/silla_gaming_813_blanco_negro_001v2_l.jpg",
  "696;Webcam 4K;75.25;Resolución Ultra HD para tus reuniones de equipo.;https://resource.logitech.com/w_80,h_50,c_limit,q_auto,f_auto,dpr_2.0/d_transparent.gif/content/dam/logitech/en/products/webcams/brio/gallery/brio-gallery-2.png?v=1",
];

let arrayObjetos = [];
let carrito = [];
arrayProductos.forEach((elemento, indice) => {
  const [id, nombre, precio, descripcion, imagen] = elemento.split(";");
  const objeto = {
    id: parseInt(id),
    nombre: nombre,
    precio: parseFloat(precio),
    descripcion: descripcion,
    imagen: imagen,
  };
  arrayObjetos.push(objeto);
});

arrayObjetos.forEach((producto, indice) => {
  dibujarProducto(producto);
});

function dibujarProducto(producto) {
  const temp = document.getElementById("plantillaTarjeta");
  const clon = temp.content.cloneNode(true);

  clon.querySelector(".product-image").src = producto.imagen;
  clon.querySelector(".product-title").textContent = producto.nombre;
  clon.querySelector(".product-desc").textContent = producto.descripcion;
  clon.querySelector(".product-price").textContent =
    producto.precio.toFixed(2) + "€";

  clon.querySelector(".add-btn").dataset.id = producto.id;
  const padre = document.querySelector("#productGrid");
  padre.appendChild(clon);
}

const iconoCarrito = document.querySelector("#iconoCarrito");
iconoCarrito.addEventListener("click", () => {
  const carritoContainer = document.querySelector("#carritoContainer");
  carritoContainer.classList.add("active");
});

const gridProductos = document.querySelector("#productGrid");
gridProductos.addEventListener("click", (e) => {
  if (e.target.classList.contains("add-btn")) {
    const productoID = e.target.dataset.id;
    añadirAlCarrito(productoID);
  }
});

function añadirAlCarrito(productoID) {
  const productoAñadir = arrayObjetos.find((p) => p.id == productoID);
  if (productoAñadir == undefined) {
    alert("Producto no encontrado");
    return;
  }
  const productoExiste = carrito.find((item) => item.id == productoID);
  if (productoExiste) {
    productoExiste.cantidad += 1;
  } else {
    const diccionarioProducto = {
      id: parseInt(productoAñadir.id),
      nombre: productoAñadir.nombre,
      precio: parseFloat(productoAñadir.precio),
      descripcion: productoAñadir.descripcion,
      imagen: productoAñadir.imagen,
      cantidad: 1,
    };
    carrito.push(diccionarioProducto);
  }
  actualizarCarrito();
}

function actualizarCarrito() {
  const badge = document.querySelector("#cartBadge");
  const contenedor = document.querySelector("#cartItems");
  const template = document.querySelector("#elementoCarrito");
  const totalDOM = document.querySelector("#totalValue");

  contenedor.innerHTML = "";

  let totalCantidad = 0;
  let totalPrecio = 0;

  carrito.forEach((item) => {
    const clon = template.content.cloneNode(true);

    clon.querySelector(".cart-item-img").src = item.imagen;
    clon.querySelector(".cart-item-title").textContent =
      `${item.nombre} x${item.cantidad}`;
    clon.querySelector(".cart-item-price").textContent =
      (item.precio * item.cantidad).toFixed(2) + "€";

    clon.querySelector(".remove-btn").dataset.id = item.id;

    contenedor.appendChild(clon);

    totalCantidad += item.cantidad;
    totalPrecio += item.precio * item.cantidad;
  });

  badge.textContent = totalCantidad;
  totalDOM.textContent = totalPrecio.toFixed(2) + "€";
}

// Cerrar y abrir el carrito
const sidebar = document.querySelector("#sidebar");
const closeCart = document.querySelector("#closeCart");

iconoCarrito.addEventListener("click", () => {
  sidebar.classList.add("active");
});

closeCart.addEventListener("click", () => {
  sidebar.classList.remove("active");
});

const btnComprar = document.querySelector("#comprarCarrito");
btnComprar.addEventListener("click", (e) => {});
// - Convierte el array de strings en un array de objetos con las propiedades: id (entero),
// nombre, precio (decimal), descripcion, imagen.
// - U%liza el <template> con id “plan%llaTarjeta” para dibujar cada producto en el grid
// (productGrid). Asigna el id del producto al atributo data-id del botón "Añadir".
// - Implementa la función para añadir productos al carrito. Se añadirán en el .html y
// también en una variable “carrito”.
// - Si el producto ya existe, incrementa su can%dad.
// - Actualiza el badge (cartBadge) con el número total de ariculos.
// - Dibuja los elementos del carrito usando el <template> con id elementoCarrito.
// - Implementa la eliminación de productos del carrito.
// - Abrir el carrito al pulsar el icono del carrito usando la clase de CSS llamada “ac%ve” y
// cierra el carrito pulsando la X de arriba a la derecha eliminando dicha clase.
// - Debe mostrarse el total de los productos comprado en el “Total” de la cesta.
// - El botón “Vaciar Cesta” elimina todos los productos de la cesta y también de la
// variable “carrito”.
// - El botón comprar mostrará un alert con el nombre del producto, la can%dad y el
// precio.
