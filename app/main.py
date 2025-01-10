from fastapi import FastAPI
from app.controllers import units_controller, products_controller, receipts_controller, sales_controller
from app.db.database import Base, engine

def create_app() -> FastAPI:
    """
    Factory function to create and configure the FastAPI application.
    """
    api = FastAPI(title="POS API", version="1.0.0")

    # Include routers
    api.include_router(units_controller.router, prefix="/units", tags=["Units"])
    api.include_router(products_controller.router, prefix="/products", tags=["Products"])
    api.include_router(receipts_controller.router, prefix="/receipts", tags=["Receipts"])
    api.include_router(sales_controller.router, prefix="/sales", tags=["Sales Reports"])

    @api.on_event("startup")
    def startup_event() -> None:
        """
        Initialize database tables during application startup.
        """
        # Ensure the tables are created during startup
        Base.metadata.create_all(bind=engine)

    @api.on_event("shutdown")
    def shutdown_event() -> None:
        """
        Perform cleanup tasks during application shutdown.
        """
        # You can add logic to clean up or close connections if needed
        pass

    return api

# Create the application instance
app = create_app()
