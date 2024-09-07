
				{
					__sveltekit_1736p27 = {
						base: new URL(".", location).pathname.slice(0, -1)
					};

					const element = document.currentScript.parentElement;

					const data = [null,null];

					Promise.all([
						import("./app/immutable/entry/start.k9NGZn5s.js"),
						import("./app/immutable/entry/app.BVwCY5W_.js")
					]).then(([kit, app]) => {
						kit.start(app, element, {
							node_ids: [0, 8],
							data,
							form: null,
							error: null
						});
					});
				}
			