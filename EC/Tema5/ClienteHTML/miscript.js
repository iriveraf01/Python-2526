const API_URL = "http://127.0.0.1:8001";

document.addEventListener("DOMContentLoaded", () => {
    const productosGrid = document.querySelector("#productos-grid");
    const productoCardTemplate = document.querySelector("#tpl-producto-card");
    const emptyState = document.querySelector("#empty-state");
    const badgeCount = document.querySelector("#badge-count");

    cargarProductos();

    document.querySelector("#btn-recargar").addEventListener("click", cargarProductos);

    async function cargarProductos() {
        try {
        const response = await fetch(`${API_URL}/productos`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });
        if (!response.ok)
            throw new Error("Error al devolver datos de los productos");
        const productos = await response.json();
        mostrarProductos(productos);
        } catch (err) {
        mostrarToast("Error al cargar productos: " + err.message, "danger");
        }
    }

    function mostrarProductos(productos) {
        // Limpia los col
        productosGrid.querySelectorAll(".col").forEach((el) => el.remove());
        //Recorro cada producto que haya
        productos.forEach((producto) => {
            const clon = productoCardTemplate.content.cloneNode(true);
            clon.querySelector("[data-field='id']").textContent = producto.id;
            clon.querySelector("[data-field='nombre']").textContent = producto.nombre;
            clon.querySelector("[data-field='precio']").textContent = producto.precio.toFixed(2) + " €";
            clon.querySelector("[data-field='descripcion']").textContent = producto.descripcion || "Sin descripción";
            // Recorro las categorías existentes y las crea
            const categoriasDiv = clon.querySelector("[data-field='categorias']");
            producto.categorias.forEach((cat) => {
                const span = document.createElement("span");
                span.classList.add("tag");
                span.textContent = cat;
                categoriasDiv.appendChild(span);
            });

            const fecha = new Date(producto.fecha_creacion).toLocaleDateString("es-ES");
            clon.querySelector("[data-field='fecha']").textContent = fecha;
            // Hace que el badge sea de color rojo amarillo o verde
            const stockBadge = clon.querySelector("[data-field='stock-badge']");
            if (producto.stock === 0) {
                stockBadge.classList.add("bg-danger");
                stockBadge.textContent = "Sin stock";
            } else if (producto.stock <= 5) {
                stockBadge.classList.add("bg-warning", "text-dark");
                stockBadge.textContent = `Stock: ${producto.stock}`;
            } else {
                stockBadge.classList.add("bg-success");
                stockBadge.textContent = `Stock: ${producto.stock}`;
            }
            // Hace que sea clicable para ver lo que tiene
            const article = clon.querySelector("article");
            article.style.cursor = "pointer";
            article.addEventListener("click", () => abrirDetalle(producto));
            // Mete el card en el html
            productosGrid.appendChild(clon);
        });
        // Actualiza el contador
        emptyState.hidden = productos.length > 0;
        badgeCount.textContent = productos.length;
        
    }
});
