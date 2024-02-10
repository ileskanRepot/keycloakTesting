{ pkgs ? import <nixpkgs> {}}:
  pkgs.mkShell {
    nativeBuildInputs = let
      env = pyPkgs : with pyPkgs; [
        fastapi
        uvicorn
        python-keycloak
      ];
    in with pkgs; [
      (python311.withPackages env)
      nodejs_21
      vite
    ];
}
