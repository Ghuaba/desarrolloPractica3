// next.config.mjs

const nextConfig = {
    distDir: 'build_node',
    env: {
        URL_API: "http://localhost:5000/" // Configuramos la dirección de la API
    },
    images: {
        domains: ['localhost'], // Permite cargar imágenes desde este dominio
    },
};

export default nextConfig;
